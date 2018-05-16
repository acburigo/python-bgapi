from struct import (unpack_from, calcsize)

from bgapi import Error


def boot(data: bytes, offset: int = 0):
    FORMAT = '<I'
    version, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {'version': version}
    return payload, offset


def boot_failure(data: bytes, offset: int = 0):
    FORMAT = '<H'
    reason, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {'reason': Error(reason)}
    return payload, offset
