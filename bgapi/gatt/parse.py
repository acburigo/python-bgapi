from struct import (unpack_from, calcsize)

from bgapi.types import MessageType

from . import rsp
from . import evt


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        0x03: rsp.discover_characteristics,
        0x04: rsp.discover_characteristics_by_uuid,
        0x06: rsp.discover_descriptors,
        0x01: rsp.discover_primary_services,
        0x02: rsp.discover_primary_services_by_uuid,
        0x0c: rsp.execute_characteristic_value_write,
        0x10: rsp.find_included_services,
        0x13: rsp.prepare_characteristic_value_reliable_write,
        0x0b: rsp.prepare_characteristic_value_write,
        0x07: rsp.read_characteristic_value,
        0x08: rsp.read_characteristic_value_by_uuid,
        0x12: rsp.read_characteristic_value_from_offset,
        0x0e: rsp.read_descriptor_value,
        0x11: rsp.read_multiple_characteristic_values,
        0x0d: rsp.send_characteristic_confirmation,
        0x05: rsp.set_characteristic_notification,
        0x00: rsp.set_max_mtu,
        0x09: rsp.write_characteristic_value,
        0x0a: rsp.write_characteristic_value_without_response,
        0x0f: rsp.write_descriptor_value,
    },

    MessageType.EVENT: {
        0x02: evt.characteristic,
        0x04: evt.characteristic_value,
        0x03: evt.descriptor,
        0x05: evt.descriptor_value,
        0x00: evt.mtu_exchanged,
        0x06: evt.procedure_completed,
        0x01: evt.service,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
