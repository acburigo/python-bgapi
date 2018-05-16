from struct import (unpack_from, calcsize)

from bgapi.base import _parse_result


def message_to_target(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    n, = unpack_from('<B', data, offset=offset)
    offset += 1
    payload = {
        'result': result,
        'data': data[offset:offset + n],
    }
    offset += n
    return payload, offset
