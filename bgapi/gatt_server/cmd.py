from struct import pack

from bgapi.base_command import command
from bgapi.types import (MessageType, MessageClass)


def find_attribute(start, type_data):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT_SERVER.value
    MSG_ID = 0x06
    payload = pack('<HB', start, len(type_data)) + bytes(type_data)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def read_attribute_type(attribute):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT_SERVER.value
    MSG_ID = 0x01
    payload = pack('<H', attribute)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def read_attribute_value(attribute, offset):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT_SERVER.value
    MSG_ID = 0x00
    payload = pack('<HH', attribute, offset)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def send_characteristic_notification(connection, characteristic, value):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT_SERVER.value
    MSG_ID = 0x05
    payload = pack('<BHB', connection, characteristic, len(value)) + bytes(value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def send_user_read_response(connection, characteristic, att_errorcode, value):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT_SERVER.value
    MSG_ID = 0x03
    payload = pack('<BHBB', connection, characteristic, att_errorcode,
                   len(value)) + bytes(value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def send_user_write_response(connection, characteristic, att_errorcode):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT_SERVER.value
    MSG_ID = 0x04
    payload = pack('<BHB', connection, characteristic, att_errorcode)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_capabilities(caps):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT_SERVER.value
    MSG_ID = 0x08
    payload = pack('<Ixxxx', caps)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def write_attribute_value(attribute, offset, value):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT_SERVER.value
    MSG_ID = 0x02
    payload = pack('<HHB', attribute, offset, len(value)) + bytes(value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
