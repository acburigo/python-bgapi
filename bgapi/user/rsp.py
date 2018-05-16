from struct import (unpack_from, calcsize)

from bgapi.base import _parse_basic_response


def _message_to_target(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    n, = unpack_from('<B', data, offset=offset)
    offset += 1
    payload.update({'data': data[offset:offset + n]})
    offset += n
    return payload, offset
