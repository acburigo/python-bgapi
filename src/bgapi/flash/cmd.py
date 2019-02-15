from struct import pack

from bgapi.base_command import command
from bgapi.types import (MessageType, MessageClass)


def ps_erase(key):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.FLASH.value
    MSG_ID = 0x04
    payload = pack('<H', key)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def ps_erase_all():
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.FLASH.value
    MSG_ID = 0x01
    payload = b''
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def ps_load(key):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.FLASH.value
    MSG_ID = 0x03
    payload = pack('<H', key)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def ps_save(key, value):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.FLASH.value
    MSG_ID = 0x02
    payload = pack('<HB', key, len(value)) + bytes(value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
