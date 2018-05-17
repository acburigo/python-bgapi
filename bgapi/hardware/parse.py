from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x0c: rsp.set_lazy_soft_timer,
        0x00: rsp.set_soft_timer,
    },

    MessageType.EVENT: {
        0x00: evt.soft_timer,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
