from struct import (unpack_from, calcsize)

from bgapi.base import _parse_result


def dtm_completed(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)

    FORMAT = '<H'
    number_of_packets, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'result': result,
        'number_of_packets': number_of_packets,
    }

    return payload, offset
