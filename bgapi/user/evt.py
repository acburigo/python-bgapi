from struct import (unpack_from, calcsize)


def message_to_host(data: bytes, offset: int = 0):
    FORMAT = '<B'
    n, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    _data = data[offset:offset + n]
    offset += n

    payload = {
        'data': _data,
    }

    return payload, offset
