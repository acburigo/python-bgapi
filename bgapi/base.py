from struct import (pack, unpack_from, calcsize, error)

import bgapi
from bgapi import (MessageType, MessageClass, Error)


PARSE_MAP = {
    MessageType.COMMAND_RESPONSE: {
        MessageClass.COEX: {
            0x01: bgapi.coex.rsp.get_counters,
            0x00: bgapi.coex.rsp.set_options,
        },

        MessageClass.DFU: {
            0x01: bgapi.dfu.rsp.flash_set_address,
            0x02: bgapi.dfu.rsp.flash_upload,
            0x03: bgapi.dfu.rsp.flash_upload_finish,
        },

        MessageClass.ENDPOINT: {
        },

        MessageClass.FLASH: {
            0x04: bgapi.flash.rsp.ps_erase,
            0x01: bgapi.flash.rsp.ps_erase_all,
            0x03: bgapi.flash.rsp.ps_load,
            0x02: bgapi.flash.rsp.ps_save,
        },

        MessageClass.GATT: {
            0x03: bgapi.gatt.rsp.discover_characteristics,
            0x04: bgapi.gatt.rsp.discover_characteristics_by_uuid,
            0x06: bgapi.gatt.rsp.discover_descriptors,
            0x01: bgapi.gatt.rsp.discover_primary_services,
            0x02: bgapi.gatt.rsp.discover_primary_services_by_uuid,
            0x0c: bgapi.gatt.rsp.execute_characteristic_value_write,
            0x10: bgapi.gatt.rsp.find_included_services,
            0x13: bgapi.gatt.rsp.prepare_characteristic_value_reliable_write,
            0x0b: bgapi.gatt.rsp.prepare_characteristic_value_write,
            0x07: bgapi.gatt.rsp.read_characteristic_value,
            0x08: bgapi.gatt.rsp.read_characteristic_value_by_uuid,
            0x12: bgapi.gatt.rsp.read_characteristic_value_from_offset,
            0x0e: bgapi.gatt.rsp.read_descriptor_value,
            0x11: bgapi.gatt.rsp.read_multiple_characteristic_values,
            0x0d: bgapi.gatt.rsp.send_characteristic_confirmation,
            0x05: bgapi.gatt.rsp.set_characteristic_notification,
            0x00: bgapi.gatt.rsp.set_max_mtu,
            0x09: bgapi.gatt.rsp.write_characteristic_value,
            0x0a: bgapi.gatt.rsp.write_characteristic_value_without_response,
            0x0f: bgapi.gatt.rsp.write_descriptor_value,
        },

        MessageClass.GATT_SERVER: {
            0x06: bgapi.gatt_server.rsp.find_attribute,
            0x01: bgapi.gatt_server.rsp.read_attribute_type,
            0x00: bgapi.gatt_server.rsp.read_attribute_value,
            0x05: bgapi.gatt_server.rsp.send_characteristic_notification,
            0x03: bgapi.gatt_server.rsp.send_user_read_response,
            0x04: bgapi.gatt_server.rsp.send_user_write_response,
            0x08: bgapi.gatt_server.rsp.set_capabilities,
            0x02: bgapi.gatt_server.rsp.write_attribute_value,
        },

        MessageClass.HARDWARE: {
            0x0c: bgapi.hardware.rsp.set_lazy_soft_timer,
            0x00: bgapi.hardware.rsp.set_soft_timer,
        },

        MessageClass.LE_CONNECTION: {
            0x04: bgapi.le_connection.rsp.close,
            0x02: bgapi.le_connection.rsp.disable_slave_latency,
            0x01: bgapi.le_connection.rsp.get_rssi,
            0x00: bgapi.le_connection.rsp.set_parameters,
            0x03: bgapi.le_connection.rsp.set_phy,
        },

        MessageClass.LE_GAP: {
            0x0c: bgapi.le_gap.rsp.bt5_set_adv_data,
            0x13: bgapi.le_gap.rsp.clear_advertise_configuration,
            0x1a: bgapi.le_gap.rsp.connect,
            0x03: bgapi.le_gap.rsp.end_procedure,
            0x0f: bgapi.le_gap.rsp.set_advertise_channel_map,
            0x12: bgapi.le_gap.rsp.set_advertise_configuration,
            0x11: bgapi.le_gap.rsp.set_advertise_phy,
            0x10: bgapi.le_gap.rsp.set_advertise_report_scan_request,
            0x0e: bgapi.le_gap.rsp.set_advertise_timing,
            0x05: bgapi.le_gap.rsp.set_conn_parameters,
            0x19: bgapi.le_gap.rsp.set_data_channel_classification,
            0x16: bgapi.le_gap.rsp.set_discovery_timing,
            0x17: bgapi.le_gap.rsp.set_discovery_type,
            0x0d: bgapi.le_gap.rsp.set_privacy_mode,
            0x14: bgapi.le_gap.rsp.start_advertising,
            0x18: bgapi.le_gap.rsp.start_discovery,
            0x15: bgapi.le_gap.rsp.stop_advertising,
        },

        MessageClass.SM: {
        },

        MessageClass.SYSTEM: {
        },

        MessageClass.TEST: {
        },

        MessageClass.USER: {
            0x00: bgapi.user.rsp.message_to_target,
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
