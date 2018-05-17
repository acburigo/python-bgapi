from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x0c: rsp.bt5_set_adv_data,
        0x13: rsp.clear_advertise_configuration,
        0x1a: rsp.connect,
        0x03: rsp.end_procedure,
        0x0f: rsp.set_advertise_channel_map,
        0x12: rsp.set_advertise_configuration,
        0x11: rsp.set_advertise_phy,
        0x10: rsp.set_advertise_report_scan_request,
        0x0e: rsp.set_advertise_timing,
        0x05: rsp.set_conn_parameters,
        0x19: rsp.set_data_channel_classification,
        0x16: rsp.set_discovery_timing,
        0x17: rsp.set_discovery_type,
        0x0d: rsp.set_privacy_mode,
        0x14: rsp.start_advertising,
        0x18: rsp.start_discovery,
        0x15: rsp.stop_advertising,
    },

    MessageType.EVENT: {
        0x01: evt.adv_timeout,
        0x02: evt.scan_request,
        0x00: evt.scan_response,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
