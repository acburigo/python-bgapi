from struct import (unpack_from, calcsize, error)

from .types import MessageClass
from . import coex
from . import dfu
from . import flash
from . import gatt
from . import gatt_server
from . import hardware
from . import le_connection
from . import le_gap
from . import sm
from . import system
from . import test
from . import user

PARSE_MAP = {
    MessageClass.COEX: coex.parse.from_binary,
    MessageClass.DFU: dfu.parse.from_binary,
    MessageClass.ENDPOINT: None,
    MessageClass.FLASH: flash.parse.from_binary,
    MessageClass.GATT: gatt.parse.from_binary,
    MessageClass.GATT_SERVER: gatt_server.parse.from_binary,
    MessageClass.HARDWARE: hardware.parse.from_binary,
    MessageClass.LE_CONNECTION: le_connection.parse.from_binary,
    MessageClass.LE_GAP: le_gap.parse.from_binary,
    MessageClass.SM: sm.parse.from_binary,
    MessageClass.SYSTEM: system.parse.from_binary,
    MessageClass.TEST: test.parse.from_binary,
    MessageClass.USER: user.parse.from_binary,
}


def from_binary(data: bytes, offset: int = 0):
    FORMAT = '<BBBB'
    _offset = offset
    try:
        msg_type, min_payload_len, msg_class, msg_id = unpack_from(
            FORMAT, data, offset=_offset)
        _offset += calcsize(FORMAT)
        payload, _offset = PARSE_MAP[msg_class](msg_type, msg_id, data, _offset)
        packet = {
            'msg_type': msg_type,
            'min_payload_len': min_payload_len,
            'msg_class': msg_class,
            'msg_id': msg_id,
            'payload': payload,
        }
        return packet, _offset
    except error:
        return None, offset
