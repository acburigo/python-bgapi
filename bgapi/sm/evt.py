from struct import (unpack_from, calcsize)


def bonded(data: bytes, offset: int = 0):
    FORMAT = '<BB'
    connection, bonding = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'bonding': bonding,
    }

    return payload, offset


def bonding_failed(data: bytes, offset: int = 0):
    FORMAT = '<BH'
    connection, reason = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'reason': reason,
    }

    return payload, offset


def confirm_bonding(data: bytes, offset: int = 0):
    FORMAT = '<Bb'
    connection, bonding_handle = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'bonding_handle': bonding_handle,
    }

    return payload, offset


def confirm_passkey(data: bytes, offset: int = 0):
    FORMAT = '<BI'
    connection, passkey = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'passkey': passkey,
    }

    return payload, offset


def list_all_bondings_complete(data: bytes, offset: int = 0):
    return {}, offset


def list_bonding_entry(data: bytes, offset: int = 0):
    FORMAT = '<B'
    bonding, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    ADDRESS_SIZE_BYTES = 6
    address = data[offset:offset + ADDRESS_SIZE_BYTES]
    offset += ADDRESS_SIZE_BYTES

    FORMAT = '<B'
    address_type, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'bonding': bonding,
        'address': address,
        'address_type': address_type,
    }

    return payload, offset


def passkey_display(data: bytes, offset: int = 0):
    FORMAT = '<BI'
    connection, passkey = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'passkey': passkey,
    }

    return payload, offset


def passkey_request(data: bytes, offset: int = 0):
    FORMAT = '<B'
    connection, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
    }

    return payload, offset
