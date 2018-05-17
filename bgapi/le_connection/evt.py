from struct import (unpack_from, calcsize)

from bgapi.base import _parse_result
from bgapi.le_gap.types import AddressType
from bgapi.le_connection.types import Security


def closed(data: bytes, offset: int = 0):
    reason, offset = _parse_result(data, offset)
    FORMAT = '<HB'
    connection, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'reason': reason,
        'connection': connection,
    }

    return payload, offset


def opened(data: bytes, offset: int = 0):
    ADDRESS_SIZE_BYTES = 6
    address = data[offset:offset + ADDRESS_SIZE_BYTES]
    offset += ADDRESS_SIZE_BYTES

    FORMAT = '<BBBBB'
    address_type, master, connection, bonding, advertiser = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'address': address,
        'address_type': address_type,
        'master': master,
        'connection': connection,
        'bonding': bonding,
        'advertiser': advertiser,
    }

    return payload, offset


def parameters(data: bytes, offset: int = 0):
    FORMAT = '<BHHHBH'
    connection, interval, latency, timeout, security_mode, txsize = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'interval': interval,
        'latency': latency,
        'timeout': timeout,
        'security_mode': security_mode,
        'txsize': txsize,
    }

    return payload, offset


def phy_status(data: bytes, offset: int = 0):
    FORMAT = '<BB'
    connection, phy = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'phy': phy,
    }

    return payload, offset


def rssi(data: bytes, offset: int = 0):
    FORMAT = '<BBb'
    connection, status, rssi = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'status': status,
        'rssi': rssi,
    }

    return payload, offset
