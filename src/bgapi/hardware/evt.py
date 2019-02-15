from struct import (unpack_from, calcsize)


def soft_timer(data: bytes, offset: int = 0):
    FORMAT = '<B'
    handle, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'handle': handle,
    }

    return payload, offset
