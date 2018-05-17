from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x04: rsp.ps_erase,
        0x01: rsp.ps_erase_all,
        0x03: rsp.ps_load,
        0x02: rsp.ps_save,
    },

    MessageType.EVENT: {
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
