from struct import pack

from bgapi import command


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
