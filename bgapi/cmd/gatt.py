from enum import (IntEnum, IntFlag)
from struct import pack

from bgapi.utils import (uuid_to_bytes, characteristic_list_to_bytes)
from bgapi.cmd import command


class AttOpcode(IntEnum):
    GATT_READ_BY_TYPE_REQUEST = 8
    GATT_READ_BY_TYPE_RESPONSE = 9
    GATT_READ_REQUEST = 10
    GATT_READ_RESPONSE = 11
    GATT_READ_BLOB_REQUEST = 12
    GATT_READ_BLOB_RESPONSE = 13
    GATT_READ_MULTIPLE_REQUEST = 14
    GATT_READ_MULTIPLE_RESPONSE = 15
    GATT_WRITE_REQUEST = 18
    GATT_WRITE_RESPONSE = 19
    GATT_WRITE_COMMAND = 82
    GATT_PREPARE_WRITE_REQUEST = 22
    GATT_PREPARE_WRITE_RESPONSE = 23
    GATT_EXECUTE_WRITE_REQUEST = 24
    GATT_EXECUTE_WRITE_RESPONSE = 25
    GATT_HANDLE_VALUE_NOTIFICATION = 27
    GATT_HANDLE_VALUE_INDICATION = 29


class ClientConfigFlag(IntFlag):
    GATT_DISABLE = 0
    GATT_NOTIFICATION = 1
    GATT_INDICATION = 2


class ExecuteWriteFlag(IntFlag):
    GATT_CANCEL = 0
    GATT_COMMIT = 1


def discover_characteristics(connection, service):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x05
    MSG_CLASS = 0x09
    MSG_ID = 0x03
    payload = pack('<BI', connection, service)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def discover_characteristics_by_uuid(connection, service, uuid):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x06
    MSG_CLASS = 0x09
    MSG_ID = 0x04
    payload = pack('<BI', connection, service) + uuid_to_bytes(uuid)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def discover_descriptors(connection, characteristic):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x03
    MSG_CLASS = 0x09
    MSG_ID = 0x06
    payload = pack('<BH', connection, characteristic)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def discover_primary_services(connection):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = 0x09
    MSG_ID = 0x01
    payload = pack('<B', connection)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def discover_primary_services_by_uuid(connection, uuid):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x09
    MSG_ID = 0x02
    payload = pack('<B', connection) + uuid_to_bytes(uuid)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def execute_characteristic_value_write(connection, flags):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x09
    MSG_ID = 0x0c
    payload = pack('<BB', connection, flags)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def find_included_services(connection, service):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x05
    MSG_CLASS = 0x09
    MSG_ID = 0x10
    payload = pack('<BI', connection, service)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def prepare_characteristic_value_reliable_write(connection, characteristic,
                                                offset, value):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x06
    MSG_CLASS = 0x09
    MSG_ID = 0x13
    payload = pack('<BHHB', connection, characteristic, offset,
                   len(value)) + value
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def prepare_characteristic_value_write(connection, characteristic, offset,
                                       value):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x06
    MSG_CLASS = 0x09
    MSG_ID = 0x0b
    payload = pack('<BHHB', connection, characteristic, offset,
                   len(value)) + value
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def read_characteristic_value(connection, characteristic):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x03
    MSG_CLASS = 0x09
    MSG_ID = 0x07
    payload = pack('<BH', connection, characteristic)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def read_characteristic_value_by_uuid(connection, service, uuid):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x06
    MSG_CLASS = 0x09
    MSG_ID = 0x08
    payload = pack('<BI', connection, service) + uuid_to_bytes(uuid)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def read_characteristic_value_from_offset(connection, characteristic, offset,
                                          maxlen):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x07
    MSG_CLASS = 0x09
    MSG_ID = 0x12
    payload = pack('<BHHH', connection, characteristic, offset, maxlen)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def read_descriptor_value(connection, descriptor):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x03
    MSG_CLASS = 0x09
    MSG_ID = 0x0e
    payload = pack('<BH', connection, descriptor)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def read_multiple_characteristic_values(connection, characteristic_list):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x09
    MSG_ID = 0x11
    payload = pack(
        '<B', connection) + characteristic_list_to_bytes(characteristic_list)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def send_characteristic_confirmation(connection):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = 0x09
    MSG_ID = 0x0d
    payload = pack('<B', connection)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_characteristic_notification(connection, characteristic, flags):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = 0x09
    MSG_ID = 0x05
    payload = pack('<BHB', connection, characteristic, flags)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_max_mtu(max_mtu):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x09
    MSG_ID = 0x00
    payload = pack('<H', max_mtu)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def write_characteristic_value(connection, characteristic, value):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = 0x09
    MSG_ID = 0x09
    payload = pack('<BHB', connection, characteristic, len(value)) + value
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def write_characteristic_value_without_response(connection, characteristic,
                                                value):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = 0x09
    MSG_ID = 0x0a
    payload = pack('<BHB', connection, characteristic, len(value)) + value
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def write_descriptor_value(connection, descriptor, value):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = 0x09
    MSG_ID = 0x0f
    payload = pack('<BHB', connection, descriptor, len(value)) + value
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
