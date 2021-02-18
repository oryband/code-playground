"""Increment counter storage implementation for cache server.

Storage implements a single "increment with ttl" action, which increments and returns
a counter by key if it's TTL didn't pass yet, otherwise it resets it back to 0
with current timestamp.

This is somewhat similiar implementation to Redis'es INCR action with expiry
but much simpler and with less features: https://redis.io/commands/INCR
"""

from collections import defaultdict
from datetime import datetime


def value(c=0, ts=None):
    """Construct and return value object for keys in store."""
    return {'counter': c, 'timestamp': ts or datetime.utcnow().timestamp()}


# internal data storage dictionary, holds stored (key, value) pairs.
#
# TODO: periodic cleanup of old unused keys by using an expiry timer
store = defaultdict(value)


def incr_with_ttl(key, ttl):
    """Increment and return counter by key if TTL haven't passed for current key.

    Reset and return counter 0 with current timestamp if TTL have passed
    or if key doesn't exist.
    """
    global store
    data = store[key]
    counter, timestamp = data['counter'], data['timestamp']
    if datetime.utcnow().timestamp() - timestamp >= ttl:
        v = value()
        counter = v['counter']
        store[key] = v
    else:
        counter += 1
        store[key] = value(counter, timestamp)

    return counter
