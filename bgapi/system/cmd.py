from struct import pack

from bgapi import command
from bgapi.utils import address_to_bytes
from bgapi.types import (MessageType, MessageClass)


def get_bt_address():
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = MessageClass.SYSTEM.value
    MSG_ID = 0x03
    payload = b''
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def get_counters(reset):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SYSTEM.value
    MSG_ID = 0x0f
    payload = pack('<B', reset)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def get_random_data(length):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SYSTEM.value
    MSG_ID = 0x0b
    payload = pack('<B', length)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def halt(halt):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SYSTEM.value
    MSG_ID = 0x0c
    payload = pack('<B', halt)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def hello():
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = MessageClass.SYSTEM.value
    MSG_ID = 0x00
    payload = b''
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def reset(dfu):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SYSTEM.value
    MSG_ID = 0x01
    payload = pack('<B', dfu)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_bt_address(address):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x06
    MSG_CLASS = MessageClass.SYSTEM.value
    MSG_ID = 0x04
    payload = address_to_bytes(address)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_device_name(type, name):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = MessageClass.SYSTEM.value
    MSG_ID = 0x0d
    payload = pack('<BB', type, len(name)) + name
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_tx_power(power):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = MessageClass.SYSTEM.value
    MSG_ID = 0x0a
    payload = pack('<H', power)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
