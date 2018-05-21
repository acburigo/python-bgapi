from struct import pack

from bgapi.base_command import command
from bgapi.utils import (uuid_to_bytes, characteristic_list_to_bytes)
from bgapi.types import (MessageType, MessageClass)


def discover_characteristics(connection, service):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x03
    payload = pack('<BI', connection, service)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def discover_characteristics_by_uuid(connection, service, uuid):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x04
    payload = pack('<BI', connection, service) + uuid_to_bytes(uuid)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def discover_descriptors(connection, characteristic):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x06
    payload = pack('<BH', connection, characteristic)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def discover_primary_services(connection):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x01
    payload = pack('<B', connection)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def discover_primary_services_by_uuid(connection, uuid):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x02
    payload = pack('<B', connection) + uuid_to_bytes(uuid)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def execute_characteristic_value_write(connection, flags):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x0c
    payload = pack('<BB', connection, flags)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def find_included_services(connection, service):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x10
    payload = pack('<BI', connection, service)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def prepare_characteristic_value_reliable_write(connection, characteristic,
                                                offset, value):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x13
    payload = pack('<BHHB', connection, characteristic, offset,
                   len(value)) + bytes(value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def prepare_characteristic_value_write(connection, characteristic, offset,
                                       value):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x0b
    payload = pack('<BHHB', connection, characteristic, offset,
                   len(value)) + bytes(value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def read_characteristic_value(connection, characteristic):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x07
    payload = pack('<BH', connection, characteristic)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def read_characteristic_value_by_uuid(connection, service, uuid):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x08
    payload = pack('<BI', connection, service) + uuid_to_bytes(uuid)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def read_characteristic_value_from_offset(connection, characteristic, offset,
                                          maxlen):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x12
    payload = pack('<BHHH', connection, characteristic, offset, maxlen)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def read_descriptor_value(connection, descriptor):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x0e
    payload = pack('<BH', connection, descriptor)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def read_multiple_characteristic_values(connection, characteristic_list):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x11
    payload = pack(
        '<B', connection) + characteristic_list_to_bytes(characteristic_list)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def send_characteristic_confirmation(connection):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x0d
    payload = pack('<B', connection)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_characteristic_notification(connection, characteristic, flags):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x05
    payload = pack('<BHB', connection, characteristic, flags)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_max_mtu(max_mtu):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x00
    payload = pack('<H', max_mtu)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def write_characteristic_value(connection, characteristic, value):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x09
    payload = pack('<BHB', connection, characteristic, len(value)) + bytes(value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def write_characteristic_value_without_response(connection, characteristic,
                                                value):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x0a
    payload = pack('<BHB', connection, characteristic, len(value)) + bytes(value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def write_descriptor_value(connection, descriptor, value):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GATT.value
    MSG_ID = 0x0f
    payload = pack('<BHB', connection, descriptor, len(value)) + bytes(value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
