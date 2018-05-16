from struct import (unpack_from, calcsize)


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

    FORMAT = '<BBB'
    address_type, bonding, n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    _data = data[offset:offset + n]
    offset += n

    payload = {
        'rssi': rssi,
        'packet_type': packet_type,
        'address': address,
        'address_type': address_type,
        'bonding': bonding,
        'data': _data,
    }

    return payload, offset
