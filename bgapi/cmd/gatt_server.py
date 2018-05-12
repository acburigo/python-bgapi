from enum import IntFlag
from struct import pack

from bgapi.cmd import command


class CharacteristicStatusFlag(IntFlag):
    CLIENT_CONFIG = 1
    CONFIRMATION = 2


def find_attribute(start, type_data):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x03
    MSG_CLASS = 0x0a
    MSG_ID = 0x06
    payload = pack('<HB', start, len(type_data)) + type_data
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def read_attribute_type(attribute):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x0a
    MSG_ID = 0x01
    payload = pack('<H', attribute)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def read_attribute_value(attribute, offset):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = 0x0a
    MSG_ID = 0x00
    payload = pack('<HH', attribute, offset)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def send_characteristic_notification(connection, characteristic, value):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = 0x0a
    MSG_ID = 0x05
    payload = pack('<BHB', connection, characteristic, len(value)) + value
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def send_user_read_response(connection, characteristic, att_errorcode, value):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x05
    MSG_CLASS = 0x0a
    MSG_ID = 0x03
    payload = pack('<BHBB', connection, characteristic, att_errorcode,
                   len(value)) + value
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def send_user_write_response(connection, characteristic, att_errorcode):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = 0x0a
    MSG_ID = 0x04
    payload = pack('<BHB', connection, characteristic, att_errorcode)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_capabilities(caps):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x08
    MSG_CLASS = 0x0a
    MSG_ID = 0x08
    payload = pack('<Ixxxx', caps)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def write_attribute_value(attribute, offset, value):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x05
    MSG_CLASS = 0x0a
    MSG_ID = 0x02
    payload = pack('<HHB', attribute, offset, len(value)) + value
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
