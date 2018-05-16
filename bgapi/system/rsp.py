from struct import (unpack_from, calcsize)

from bgapi.base import _parse_result


def _get_bt_address(data: bytes, offset: int = 0):
    ADDRESS_SIZE_BYTES = 6
    return {'address': data[offset:offset + ADDRESS_SIZE_BYTES]}


def _get_counters(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    FORMAT = '<HHHH'
    tx_packets, rx_packets, crc_errors, failures = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'tx_packets': tx_packets,
        'rx_packets': rx_packets,
        'crc_errors': crc_errors,
        'failures': failures,
    }
    return payload, offset


def _get_random_data(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    n, = unpack_from('<B', data, offset=offset)
    offset += 1
    payload = {
        'result': result,
        'data': data[offset:offset + n],
    }
    offset += n
    return payload, offset


def _halt(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _hello(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _set_bt_address(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _set_device_name(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _set_tx_power(data: bytes, offset: int = 0):
    FORMAT = '<H'
    set_power, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    return {'set_power': set_power}, offset
