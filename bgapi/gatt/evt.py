from struct import (unpack_from, calcsize)


def characteristic(data: bytes, offset: int = 0):
    FORMAT = '<BHBB'
    connection, characteristic, properties, n = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    uuid = data[offset:offset + n]
    offset += n

    payload = {
        'connection': connection,
        'characteristic': characteristic,
        'properties': properties,
        'uuid': uuid,
    }

    return payload, offset


def characteristic_value(data: bytes, offset: int = 0):
    FORMAT = '<BHBHB'
    connection, characteristic, att_opcode, _offset, n = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    value = data[offset:offset + n]
    offset += n

    payload = {
        'connection': connection,
        'characteristic': characteristic,
        'att_opcode': att_opcode,
        'offset': _offset,
        'value': value,
    }

    return payload, offset


def descriptor(data: bytes, offset: int = 0):
    FORMAT = '<BHB'
    connection, descriptor, n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    uuid = data[offset:offset + n]
    offset += n

    payload = {
        'connection': connection,
        'descriptor': descriptor,
        'uuid': uuid,
    }

    return payload, offset


def descriptor_value(data: bytes, offset: int = 0):
    FORMAT = '<BHHB'
    connection, descriptor, _offset, n = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    value = data[offset:offset + n]
    offset += n

    payload = {
        'connection': connection,
        'descriptor': descriptor,
        'offset': _offset,
        'value': value,
    }

    return payload, offset


def mtu_exchanged(data: bytes, offset: int = 0):
    FORMAT = '<BH'
    connection, mtu = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'mtu': mtu,
    }

    return payload, offset


def procedure_completed(data: bytes, offset: int = 0):
    FORMAT = '<BH'
    connection, result = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'result': result,
    }

    return payload, offset


def service(data: bytes, offset: int = 0):
    FORMAT = '<BHB'
    connection, service, n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    uuid = data[offset:offset + n]
    offset += n

    payload = {
        'connection': connection,
        'service': service,
        'uuid': uuid,
    }

    return payload, offset
