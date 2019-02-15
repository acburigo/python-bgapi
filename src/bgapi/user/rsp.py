from struct import (unpack_from, calcsize, error)


def message_to_target(data: bytes, offset: int = 0):
    FORMAT = '<HB'
    result, n, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    _data = data[offset:offset + n]
    offset += n

    if len(_data) < n:
        raise error

    payload = {
        'result': result,
        'data': _data,
    }
    return payload, offset
