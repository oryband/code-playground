"""Simple in-memory store server implementation, with a single "increment with ttl" action.

This server app exposes a single HTTP method: GET /incr
It increments and returns given key's counter according to ttl, or resets
it back to 0 otherwise.
"""
from aiohttp import web

from store import incr_with_ttl


def validate_params(req):
    try:
        key = req.query['key']
    except KeyError:
        err = web.json_response(
            data={'status': 'error',
                  'description': 'missing query parameter \'key\''},
            status=400)
        return None, None, err

    try:
        ttl = req.query['ttl']
    except KeyError:
        err = web.json_response(
            data={'status': 'error',
                  'description': 'missing query parameter \'ttl\''},
            status=400)
        return None, None, err

    try:
        ttl = int(ttl)
    except ValueError:
        err = web.json_response(
            data={'status': 'error',
                  'description': '\'ttl\' query parameter must be an integer'},
            status=400)
        return None, None, err

    return key, ttl, None


async def incr(req):
    """Return value from store by given key if exists, else return current epoch timestamp.

    The endpoint receives two query parameters:
        1. 'key' (required)
        2. 'value' (optional, default: current epoch timestamp).

    The old value is returned from the store and the new value is set in the store instead.
    If the key doesn't exist, the default value which is current epoch timestamp is returned.
    """
    key, ttl, err = validate_params(req)
    if err is not None:
        return err

    counter = incr_with_ttl(key, ttl)
    return web.json_response(data={'status': 'success', 'counter': counter})


# main web server application object
app = web.Application()
app.add_routes([web.get('/incr', incr)])


if __name__ == '__main__':
    web.run_app(app)
