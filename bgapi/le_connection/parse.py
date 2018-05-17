from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x04: rsp.close,
        0x02: rsp.disable_slave_latency,
        0x01: rsp.get_rssi,
        0x00: rsp.set_parameters,
        0x03: rsp.set_phy,
    },

    MessageType.EVENT: {
        0x01: evt.closed,
        0x00: evt.opened,
        0x02: evt.parameters,
        0x04: evt.phy_status,
        0x03: evt.rssi,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
