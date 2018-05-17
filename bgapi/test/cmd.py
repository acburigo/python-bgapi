from struct import pack

from bgapi.base_command import command
from bgapi.types import (MessageType, MessageClass)


def dtm_end(data):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = MessageClass.TEST.value
    MSG_ID = 0x02
    payload = b''
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def dtm_rx(channel, phy):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = MessageClass.TEST.value
    MSG_ID = 0x01
    payload = pack('<BB', channel, phy)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def dtm_tx(packet_type, length, channel, phy):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = MessageClass.TEST.value
    MSG_ID = 0x00
    payload = pack('<BBBB', packet_type, length, channel, phy)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
