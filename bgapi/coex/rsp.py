from struct import (unpack_from, calcsize)


def get_counters(data: bytes, offset: int = 0):
    FORMAT = '<HB'
    result, n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    counters = unpack_from('<%dB' % n, data, offset=offset)
    payload = {
        'result': result,
        'counters': list(counters),
    }
    offset += n
    return payload, offset


def set_options(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset
