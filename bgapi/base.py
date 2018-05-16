from struct import (pack, unpack_from, calcsize, error)

import bgapi
from bgapi import (MessageType, MessageClass, Error)


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        MessageClass.COEX: {
        },

        MessageClass.DFU: {
        },

        MessageClass.ENDPOINT: {
        },

        MessageClass.FLASH: {
        },

        MessageClass.GATT: {
        },

        MessageClass.GATT_SERVER: {
        },

        MessageClass.HARDWARE: {
        },

        MessageClass.LE_CONNECTION: {
        },

        MessageClass.LE_GAP: {
        },

        MessageClass.SM: {
        },

        MessageClass.SYSTEM: {
        },

        MessageClass.TEST: {
        },

        MessageClass.USER: {
        },
    },

    MessageType.EVENT: {
        MessageClass.COEX: {
        },

        MessageClass.DFU: {
            0x00: bgapi.dfu.evt.boot,
            0x01: bgapi.dfu.evt.boot_failure,
        },

        MessageClass.ENDPOINT: {
        },

        MessageClass.FLASH: {
        },

        MessageClass.GATT: {
            0x02: bgapi.gatt.evt.characteristic,
            0x04: bgapi.gatt.evt.characteristic_value,
            0x03: bgapi.gatt.evt.descriptor,
            0x05: bgapi.gatt.evt.descriptor_value,
            0x00: bgapi.gatt.evt.mtu_exchanged,
            0x06: bgapi.gatt.evt.procedure_completed,
            0x01: bgapi.gatt.evt.service,
        },

        MessageClass.GATT_SERVER: {
            0x00: bgapi.gatt_server.evt.attribute_value,
            0x03: bgapi.gatt_server.evt.characteristic_status,
            0x04: bgapi.gatt_server.evt.execute_write_completed,
            0x01: bgapi.gatt_server.evt.user_read_request,
            0x02: bgapi.gatt_server.evt.user_write_request,
        },

        MessageClass.HARDWARE: {
            0x00: bgapi.hardware.evt.soft_timer,
        },

        MessageClass.LE_CONNECTION: {
            0x01: bgapi.le_connection.evt.closed,
            0x00: bgapi.le_connection.evt.opened,
            0x02: bgapi.le_connection.evt.parameters,
            0x04: bgapi.le_connection.evt.phy_status,
            0x03: bgapi.le_connection.evt.rssi,
        },

        MessageClass.LE_GAP: {
            0x01: bgapi.le_gap.evt.adv_timeout,
            0x02: bgapi.le_gap.evt.scan_request,
            0x00: bgapi.le_gap.evt.scan_response,
        },

        MessageClass.SM: {
            0x03: bgapi.sm.evt.bonded,
            0x04: bgapi.sm.evt.bonding_failed,
            0x09: bgapi.sm.evt.confirm_bonding,
            0x02: bgapi.sm.evt.confirm_passkey,
            0x06: bgapi.sm.evt.list_all_bondings_complete,
            0x05: bgapi.sm.evt.list_bonding_entry,
            0x00: bgapi.sm.evt.passkey_display,
            0x01: bgapi.sm.evt.passkey_request,
        },

        MessageClass.SYSTEM: {
            0x04: bgapi.system.evt.awake,
            0x00: bgapi.system.evt.boot,
            0x06: bgapi.system.evt.error,
            0x03: bgapi.system.evt.external_signal,
            0x05: bgapi.system.evt.hardware_error,
        },

        MessageClass.TEST: {
            0x00: bgapi.test.evt.dtm_completed,
        },

        MessageClass.USER: {
            0x00: bgapi.user.evt.message_to_host,
        },
    },
}


def command(msg_type, min_payload_length, msg_class, msg_id, payload=b''):
    b = pack('<BBBB', msg_type, min_payload_length, msg_class, msg_id)
    b += payload
    return b


def from_binary(data: bytes):
    FORMAT = '<BBBB'
    try:
        msg_type, min_payload_len, msg_class, msg_id = unpack_from(FORMAT, data)
        msg_type = MessageType(msg_type)
        msg_class = MessageClass(msg_class)
        payload, offset = PARSE_MAP[msg_type][msg_class][msg_id](
            data, offset=calcsize(FORMAT))
        return {
            'msg_type': msg_type,
            'min_payload_len': min_payload_len,
            'msg_class': msg_class,
            'msg_id': msg_id,
            'payload': payload,
        }, offset
    except error:
        return None, 0


def _parse_result(data: bytes, offset: int):
    FORMAT = '<H'
    result = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    return Error(result), offset
