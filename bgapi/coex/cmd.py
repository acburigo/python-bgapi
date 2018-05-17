from struct import pack

from bgapi.base_command import command
from bgapi.types import (MessageType, MessageClass)


def get_counters(reset):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x03
    MSG_CLASS = MessageClass.COEX.value
    MSG_ID = 0x01
    payload = pack('<B', reset)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_options(mask, options):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x08
    MSG_CLASS = MessageClass.COEX.value
    MSG_ID = 0x00
    payload = pack('<II', mask, options)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
