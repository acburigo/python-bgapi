from struct import (unpack_from, calcsize)


def message_to_target(data: bytes, offset: int = 0):
    FORMAT = '<HB'
    result, n, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'data': data[offset:offset + n],
    }
    offset += n
    return payload, offset
