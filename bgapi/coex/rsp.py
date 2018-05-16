from struct import (unpack_from, calcsize)

from bgapi.base import _parse_result


def _get_counters(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    FORMAT = '<B'
    n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    counters = unpack_from('<%dB' % n, data, offset=offset)
    payload = {
        'result': result,
        'counters': list(counters),
    }
    offset += n
    return payload, offset


def _set_options(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset
