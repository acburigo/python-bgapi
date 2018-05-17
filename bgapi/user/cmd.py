from struct import pack

from bgapi import command
from bgapi.types import (MessageType, MessageClass)


def message_to_target(data):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.USER.value
    MSG_ID = 0x00
    payload = pack('<B', len(data)) + data
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
