from struct import (unpack_from, calcsize)

from bgapi.base import _parse_result


def _ps_erase(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _ps_erase_all(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _ps_load(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    FORMAT = '<B'
    n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'value': data[offset:offset + n],
    }
    offset += n
    return payload, offset


def _ps_save(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset
