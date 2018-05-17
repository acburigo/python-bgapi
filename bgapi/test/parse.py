from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x02: rsp.dtm_end,
        0x01: rsp.dtm_rx,
        0x00: rsp.dtm_tx,
    },

    MessageType.EVENT: {
        0x00: evt.dtm_completed,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
