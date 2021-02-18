#!/usr/bin/env python
"""Simple HTTP client "DoS" implementation using asyncio and aiohttp.

This application generates multiple "clients" that periodically send
HTTP requests to a server, sleep randomly, and retry.
"""
import asyncio
import logging
from enum import Enum
from random import randint, seed

import aiohttp

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


# TODO: use configuration file and environment variables
CLIENTS = 200
SERVER_URL = 'http://localhost:8000'
SLEEP_RANGE = 7  # max sleep in seconds


class TaskType(Enum):
    """Enum denoting async task types used in this application."""

    REQUEST = 1
    SLEEP = 2


# TODO: error handling
async def send_request(session):
    """Generate a random client id and send an HTTP request to the server.

    Returns a task identifier, denoting this was a "Send Request" task that had just ended.
    """
    client_id = randint(0, CLIENTS)
    logging.info('sending request to %s/?clientId=%d', SERVER_URL, client_id)
    async with session.get(SERVER_URL, params=[('clientId', client_id)]) as _:
        pass
    return TaskType.REQUEST


async def random_sleep():
    """Sleep a random amount of time according to configurable sleep range.

    Returns a task identifier, denoting this was a "Random Sleep" task that had just ended.
    """
    await asyncio.sleep(randint(0, SLEEP_RANGE))
    return TaskType.SLEEP


async def dos():
    """Infinitely send HTTP requests and sleep until cancelled."""
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=CLIENTS))
    async with session:
        # initialize first requests
        pending = [asyncio.shield(asyncio.create_task(send_request(session))) for _ in range(CLIENTS)]

        while True:
            # wait for the first async task to complete
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            for future in done:
                # if we should exit, wait for pending tasks to finish and return.
                if future.cancelled():
                    asyncio.gather(*pending)
                    return

                # for every finished request task, schedule a random sleep task, and vice versa
                if await future == TaskType.REQUEST:
                    pending.add(asyncio.shield(asyncio.create_task(random_sleep())))
                else:  # TaskType.SLEEP
                    pending.add(asyncio.shield(asyncio.create_task(send_request(session))))


async def main():
    try:
        task = await asyncio.create_task(dos())
    except KeyboardInterrupt:
        logging.info('Shutting down...')
        task.cancel()
        await task


if __name__ == '__main__':
    # seed randomness for random sleep and client ids
    seed()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
