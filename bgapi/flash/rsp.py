from struct import (unpack_from, calcsize)

from bgapi.base import _parse_basic_response


def _ps_erase(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _ps_erase_all(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _ps_load(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    FORMAT = '<B'
    n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload.update({'value': data[offset:offset+n]})
    offset += n
    return payload, offset


def _ps_save(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)
