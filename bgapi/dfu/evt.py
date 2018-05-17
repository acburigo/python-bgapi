from struct import (unpack_from, calcsize)

from bgapi import Error
from bgapi.base import _parse_result


def boot(data: bytes, offset: int = 0):
    FORMAT = '<I'
    version, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {'version': version}
    return payload, offset


def boot_failure(data: bytes, offset: int = 0):
    reason, offset = _parse_result(data, offset)
    payload = {'reason': reason}
    return payload, offset
