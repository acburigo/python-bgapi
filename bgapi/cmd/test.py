from enum import IntEnum
from struct import pack

from bgapi.cmd import command


class PacketType(IntEnum):
    PKT_PRBS9 = 0
    PKT_11110000 = 1
    PKT_10101010 = 2
    PKT_CARRIER_DEPRECATED = 3
    PKT_11111111 = 4
    PKT_00000000 = 5
    PKT_00001111 = 6
    PKT_01010101 = 7
    PKT_PN9 = 253
    PKT_CARRIER = 254


class Phy(IntEnum):
    PHY_1M = 1
    PHY_2M = 2
    PHY_125K = 3
    PHY_500K = 4


def dtm_end(data):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = 0x0e
    MSG_ID = 0x02
    payload = b''
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def dtm_rx(channel, phy):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x0e
    MSG_ID = 0x01
    payload = pack('<BB', channel, phy)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def dtm_tx(packet_type, length, channel, phy):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = 0x0e
    MSG_ID = 0x00
    payload = pack('<BBBB', packet_type, length, channel, phy)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
