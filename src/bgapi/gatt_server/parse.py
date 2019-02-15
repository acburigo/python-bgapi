from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x06: rsp.find_attribute,
        0x01: rsp.read_attribute_type,
        0x00: rsp.read_attribute_value,
        0x05: rsp.send_characteristic_notification,
        0x03: rsp.send_user_read_response,
        0x04: rsp.send_user_write_response,
        0x08: rsp.set_capabilities,
        0x02: rsp.write_attribute_value,
    },

    MessageType.EVENT: {
        0x00: evt.attribute_value,
        0x03: evt.characteristic_status,
        0x04: evt.execute_write_completed,
        0x01: evt.user_read_request,
        0x02: evt.user_write_request,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
