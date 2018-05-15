from struct import (unpack_from, calcsize)

from bgapi.base import _parse_basic_response


def _find_attribute(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    FORMAT = '<H'
    sent_len, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload.update({'sent_len': sent_len})
    return payload, offset


def _read_attribute_type(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    FORMAT = '<B'
    n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload.update({'type': data[offset:offset+n]})
    offset += n
    return payload, offset


def _read_attribute_value(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    FORMAT = '<B'
    n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload.update({'value': data[offset:offset+n]})
    offset += n
    return payload, offset


def _send_characteristic_notification(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    FORMAT = '<H'
    sent_len, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload.update({'sent_len': sent_len})
    return payload, offset


def _send_user_read_response(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    FORMAT = '<H'
    sent_len, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload.update({'sent_len': sent_len})
    return payload, offset


def _send_user_write_response(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_capabilities(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _write_attribute_value(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)
