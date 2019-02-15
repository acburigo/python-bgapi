from struct import (unpack_from, calcsize, error)


def attribute_value(data: bytes, offset: int = 0):
    FORMAT = '<BHBHB'
    connection, attribute, att_opcode, _offset, n = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    value = data[offset:offset + n]
    offset += n

    if len(value) < n:
        raise error

    payload = {
        'connection': connection,
        'attribute': attribute,
        'att_opcode': att_opcode,
        'offset': _offset,
        'value': value,
    }

    return payload, offset


def characteristic_status(data: bytes, offset: int = 0):
    FORMAT = '<BHBH'
    connection, characteristic, status_flags, client_config_flags = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'characteristic': characteristic,
        'status_flags': status_flags,
        'client_config_flags': client_config_flags,
    }

    return payload, offset


def execute_write_completed(data: bytes, offset: int = 0):
    FORMAT = '<BH'
    connection, result = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'result': result,
    }

    return payload, offset


def user_read_request(data: bytes, offset: int = 0):
    FORMAT = '<BHBH'
    connection, characteristic, att_opcode, _offset = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'characteristic': characteristic,
        'att_opcode': att_opcode,
        'offset': _offset,
    }

    return payload, offset


def user_write_request(data: bytes, offset: int = 0):
    FORMAT = '<BHBHB'
    connection, characteristic, att_opcode, _offset, n = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    value = data[offset:offset + n]
    offset += n

    if len(value) < n:
        raise error

    payload = {
        'connection': connection,
        'characteristic': characteristic,
        'att_opcode': att_opcode,
        'offset': _offset,
        'value': value,
    }

    return payload, offset
