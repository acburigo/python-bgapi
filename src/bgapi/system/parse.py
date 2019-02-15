from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x03: rsp.get_bt_address,
        0x0f: rsp.get_counters,
        0x0b: rsp.get_random_data,
        0x0c: rsp.halt,
        0x00: rsp.hello,
        0x04: rsp.set_bt_address,
        0x0d: rsp.set_device_name,
        0x0a: rsp.set_tx_power,
    },

    MessageType.EVENT: {
        0x04: evt.awake,
        0x00: evt.boot,
        0x06: evt.error,
        0x03: evt.external_signal,
        0x05: evt.hardware_error,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
