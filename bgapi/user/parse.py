from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x00: rsp.message_to_target,
    },

    MessageType.EVENT: {
        0x00: evt.message_to_host,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
