from struct import (unpack_from, calcsize)

from bgapi.base import _parse_basic_response


def _bonding_confirm(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _configure(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _delete_bonding(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _delete_bondings(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _enter_passkey(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _increase_security(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _list_all_bondings(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _passkey_confirm(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_bondable_mode(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_debug_mode(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_oob_data(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_passkey(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_sc_remote_oob_data(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _store_bonding_configuration(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _use_sc_oob(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    SIZE_BYTES = 32
    payload.update({'oob_data': data[offset:offset + SIZE_BYTES]})
    offset += SIZE_BYTES
    return payload, offset
