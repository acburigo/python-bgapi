from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x01: rsp.flash_set_address,
        0x02: rsp.flash_upload,
        0x03: rsp.flash_upload_finish,
    },

    MessageType.EVENT: {
        0x00: evt.boot,
        0x01: evt.boot_failure,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
