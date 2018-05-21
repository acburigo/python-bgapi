import struct
from struct import (unpack_from, calcsize)


def awake(data: bytes, offset: int = 0):
    return {}, offset


def boot(data: bytes, offset: int = 0):
    FORMAT = '<HHHHIHI'
    major, minor, patch, build, bootloader, hw, hash = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'major': major,
        'minor': minor,
        'patch': patch,
        'build': build,
        'bootloader': bootloader,
        'hw': hw,
        'hash': hash,
    }

    return payload, offset


def error(data: bytes, offset: int = 0):
    FORMAT = '<HB'
    reason, n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    _data = data[offset:offset + n]
    offset += n

    if len(_data) < n:
        raise struct.error

    payload = {
        'reason': reason,
        'data': _data,
    }

    return payload, offset


def external_signal(data: bytes, offset: int = 0):
    FORMAT = '<I'
    extsignals, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'extsignals': extsignals,
    }

    return payload, offset


def hardware_error(data: bytes, offset: int = 0):
    FORMAT = '<H'
    status, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'status': status,
    }
    return payload, offset
