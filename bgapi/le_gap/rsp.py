from struct import (unpack_from, calcsize)

from bgapi.base import _parse_basic_response


def _bt5_set_adv_data(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _clear_advertise_configuration(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _connect(data: bytes, offset: int = 0):
    payload, offset = _parse_basic_response(data, offset)
    FORMAT = '<B'
    connection, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload.update({'connection': connection})
    return payload, offset


def _end_procedure(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_advertise_channel_map(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_advertise_configuration(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_advertise_phy(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_advertise_report_scan_request(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_advertise_timing(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_conn_parameters(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_data_channel_classification(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_discovery_timing(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_discovery_type(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_privacy_mode(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _start_advertising(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _start_discovery(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _stop_advertising(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)
