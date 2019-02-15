from struct import (unpack_from, calcsize, error)


def adv_timeout(data: bytes, offset: int = 0):
    FORMAT = '<B'
    handle, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'handle': handle,
    }

    return payload, offset


def scan_request(data: bytes, offset: int = 0):
    FORMAT = '<B'
    handle, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    ADDRESS_SIZE_BYTES = 6
    address = data[offset:offset + ADDRESS_SIZE_BYTES]
    offset += ADDRESS_SIZE_BYTES

    if len(address) < ADDRESS_SIZE_BYTES:
        raise error

    FORMAT = '<BB'
    address_type, bonding = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'handle': handle,
        'address': address,
        'address_type': address_type,
        'bonding': bonding,
    }

    return payload, offset


def scan_response(data: bytes, offset: int = 0):
    FORMAT = '<bB'
    rssi, packet_type = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    ADDRESS_SIZE_BYTES = 6
    address = data[offset:offset + ADDRESS_SIZE_BYTES]
    offset += ADDRESS_SIZE_BYTES

    if len(address) < ADDRESS_SIZE_BYTES:
        raise error

    FORMAT = '<BBB'
    address_type, bonding, n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    _data = data[offset:offset + n]
    offset += n

    if len(_data) < n:
        raise error

    payload = {
        'rssi': rssi,
        'packet_type': packet_type,
        'address': address,
        'address_type': address_type,
        'bonding': bonding,
        'data': _data,
    }

    return payload, offset
