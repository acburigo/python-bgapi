from enum import IntEnum
from struct import (pack, unpack_from, calcsize, error)


class MessageType(IntEnum):
    COMMAND_RESPONSE = 0x20
    EVENT = 0xa0


class MessageClass(IntEnum):
    COEX = 0x20
    DFU = 0x00
    ENDPOINT = 0x0b
    FLASH = 0x0d
    GATT = 0x09
    GATT_SERVER = 0x0a
    HARDWARE = 0x0c
    LE_CONNECTION = 0x08
    LE_GAP = 0x03
    SM = 0x0f
    SYSTEM = 0x01
    TEST = 0x0e
    USER = 0xff


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        MessageClass.COEX: {
        },

        MessageClass.DFU: {
        },

        MessageClass.ENDPOINT: {
        },

        MessageClass.FLASH: {
        },

        MessageClass.GATT: {
        },

        MessageClass.GATT_SERVER: {
        },

        MessageClass.HARDWARE: {
        },

        MessageClass.LE_CONNECTION: {
        },

        MessageClass.LE_GAP: {
        },

        MessageClass.SM: {
        },

        MessageClass.SYSTEM: {
        },

        MessageClass.TEST: {
        },

        MessageClass.USER: {
        },
    },

    MessageType.EVENT: {
        MessageClass.COEX: {
        },

        MessageClass.DFU: {
        },

        MessageClass.ENDPOINT: {
        },

        MessageClass.FLASH: {
        },

        MessageClass.GATT: {
        },

        MessageClass.GATT_SERVER: {
        },

        MessageClass.HARDWARE: {
        },

        MessageClass.LE_CONNECTION: {
        },

        MessageClass.LE_GAP: {
        },

        MessageClass.SM: {
        },

        MessageClass.SYSTEM: {
        },

        MessageClass.TEST: {
        },

        MessageClass.USER: {
        },
    },
}


def command(msg_type, min_payload_length, msg_class, msg_id, payload=b''):
    b = pack('<BBBB', msg_type, min_payload_length, msg_class, msg_id)
    b += payload
    return b


def from_binary(data: bytes):
    FORMAT = '<BBBB'
    try:
        msg_type, min_payload_len, msg_class, msg_id = unpack_from(FORMAT, data)
        msg_type = MessageType(msg_type)
        msg_class = MessageClass(msg_class)
        payload, offset = PARSE_MAP[msg_type][msg_class][msg_id](
            data, offset=calcsize(FORMAT))
        return {
            'msg_type': msg_type,
            'min_payload_len': min_payload_len,
            'msg_class': msg_class,
            'msg_id': msg_id,
            'payload': payload,
        }, offset
    except error:
        return None, 0
