from struct import (unpack_from, calcsize)


def dtm_completed(data: bytes, offset: int = 0):
    FORMAT = '<HH'
    result, number_of_packets = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'result': result,
        'number_of_packets': number_of_packets,
    }

    return payload, offset
