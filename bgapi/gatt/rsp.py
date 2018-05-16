from struct import (unpack_from, calcsize)

from bgapi.base import _parse_result


def _discover_characteristics(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _discover_characteristics_by_uuid(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _discover_descriptors(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _discover_primary_services(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _discover_primary_services_by_uuid(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _execute_characteristic_value_write(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _find_included_services(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _prepare_characteristic_value_reliable_write(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    FORMAT = '<H'
    sent_len, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'sent_len': sent_len,
    }
    return payload, offset


def _prepare_characteristic_value_write(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    FORMAT = '<H'
    sent_len, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'sent_len': sent_len,
    }
    return payload, offset


def _read_characteristic_value(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _read_characteristic_value_by_uuid(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _read_characteristic_value_from_offset(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _read_descriptor_value(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _read_multiple_characteristic_values(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _send_characteristic_confirmation(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _set_characteristic_notification(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _set_max_mtu(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    FORMAT = '<H'
    max_mtu, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'max_mtu': max_mtu,
    }
    return payload, offset


def _write_characteristic_value(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _write_characteristic_value_without_response(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    FORMAT = '<H'
    sent_len, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'sent_len': sent_len,
    }
    return payload, offset


def _write_descriptor_value(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset
