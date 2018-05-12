from enum import IntEnum
from struct import pack

from bgapi.cmd import command


class Security(IntEnum):
    MODE1_LEVEL1 = 0
    MODE1_LEVEL2 = 1
    MODE1_LEVEL3 = 2
    MODE1_LEVEL4 = 3


def close(connection):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = 0x08
    MSG_ID = 0x04
    payload = pack('<B', connection)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def disable_slave_latency(connection, disable):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x08
    MSG_ID = 0x02
    payload = pack('<BB', connection, disable)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def get_rssi(connection):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = 0x08
    MSG_ID = 0x01
    payload = pack('<B', connection)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_parameters(connection, min_interval, max_interval, latency, timeout):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x09
    MSG_CLASS = 0x08
    MSG_ID = 0x00
    payload = pack('<BHHHH', connection, min_interval, max_interval, latency,
                   timeout)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_phy(connection, phy):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x08
    MSG_ID = 0x03
    payload = pack('<BB', connection, phy)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
