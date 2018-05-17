from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x0e: rsp.bonding_confirm,
        0x01: rsp.configure,
        0x06: rsp.delete_bonding,
        0x07: rsp.delete_bondings,
        0x08: rsp.enter_passkey,
        0x04: rsp.increase_security,
        0x0b: rsp.list_all_bondings,
        0x09: rsp.passkey_confirm,
        0x00: rsp.set_bondable_mode,
        0x0f: rsp.set_debug_mode,
        0x0a: rsp.set_oob_data,
        0x10: rsp.set_passkey,
        0x12: rsp.set_sc_remote_oob_data,
        0x02: rsp.store_bonding_configuration,
        0x11: rsp.use_sc_oob,
    },

    MessageType.EVENT: {
        0x03: evt.bonded,
        0x04: evt.bonding_failed,
        0x09: evt.confirm_bonding,
        0x02: evt.confirm_passkey,
        0x06: evt.list_all_bondings_complete,
        0x05: evt.list_bonding_entry,
        0x00: evt.passkey_display,
        0x01: evt.passkey_request,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
