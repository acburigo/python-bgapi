from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x01: rsp.get_counters,
        0x00: rsp.set_options,
    },

    MessageType.EVENT: {
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
