#!/usr/bin/env python
"""Main server implementation for assignment, with fixed window rate limiting.

This implementation exposes a single endpoint: GET /?clientId=<int> (root endpoint)
It returns HTTP 200 OK if client has not exceeded its request rate limit in current
fixed window.

This applications depends on a simple storage server,
which functions as the rate limit memory.
"""
from aiohttp import ClientSession, web


# TODO: use configuration file and support environment variables
CACHE_URL = 'http://localhost:8001'
RATE_LIMIT_WINDOW_LENGTH = 5
RATE_LIMIT_MAX_REQ_IN_WINDOW = 5


# TODO: app - cache HTTP error handling
async def incr(client_id):
    """Increment and return client_id rate limit counter.

    Counter is fetched from storage service.
    """
    async with ClientSession() as session:
        async with session.get('{}/incr'.format(app['cache_url']),
                               params=[('key', client_id),
                                       ('ttl', RATE_LIMIT_WINDOW_LENGTH)]) as resp:

            return (await resp.json())["counter"]


def validate_params(req):
    try:
        client_id = req.query['clientId']
    except KeyError:
        err = web.json_response(
            data={'error': 'missing query parameter clientId=<int>'},
            status=400)

        return None, err

    if client_id == '':
        err = web.json_response(
            data={'error': 'query parameter clientId value must be a non-empty string'},
            status=400)

        return None, err

    return client_id, None


async def root(req):
    """Return HTTP 200 OK if client id is within its rate limit window and count.

    Return HTTP 503 Service Unavailable otherwise.
    """
    client_id, err = validate_params(req)
    if err is not None:
        return err

    counter = await incr(client_id)

    if counter >= RATE_LIMIT_MAX_REQ_IN_WINDOW:
        return web.Response(status=503)

    return web.Response(status=200)


app = web.Application()
app.add_routes([web.get('/', root)])
# TODO: configurable
# TODO: normalize URL
app['cache_url'] = CACHE_URL


if __name__ == '__main__':
    web.run_app(app)
