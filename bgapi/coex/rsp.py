from struct import (unpack_from, calcsize)

from bgapi.base import _parse_basic_response


def _get_counters(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    FORMAT = '<B'
    n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    counters = unpack_from('<%dB' % n, data, offset=offset)
    payload.update({'counters': list(counters)})
    offset += n
    return payload, offset


def _set_options(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)
