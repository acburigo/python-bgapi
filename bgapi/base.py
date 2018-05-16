from struct import (pack, unpack_from, calcsize, error)

from bgapi import (MessageType, MessageClass, Error)


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


def _parse_basic_response(data: bytes, offset: int):
    FORMAT = '<H'
    result = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    return {
        'result': Error(result),
    }
