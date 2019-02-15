from struct import pack

from bgapi.base_command import command
from bgapi.utils import address_to_bytes
from bgapi.types import (MessageType, MessageClass)


def bt5_set_adv_data(handle, scan_rsp, adv_data):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x0c
    payload = pack('<BBB', handle, scan_rsp, len(adv_data)) + bytes(adv_data)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def clear_advertise_configuration(handle, configurations):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x13
    payload = pack('<BI', handle, configurations)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def connect(address, address_type, initiating_phy):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x1a
    payload = address_to_bytes(address) + pack('<BB', address_type,
                                               initiating_phy)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def end_procedure():
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x03
    payload = b''
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_advertise_channel_map(handle, channel_map):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x0f
    payload = pack('<BB', handle, channel_map)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_advertise_configuration(handle, configurations):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x12
    payload = pack('<BI', handle, configurations)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_advertise_phy(handle, primary_phy, secondary_phy):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x11
    payload = pack('<BBB', handle, primary_phy, secondary_phy)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_advertise_report_scan_request(handle, report_scan_req):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x10
    payload = pack('<BB', handle, report_scan_req)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_advertise_timing(handle, interval_min, interval_max, duration,
                         maxevents):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x0e
    payload = pack('<BIIHB', handle, interval_min, interval_max, duration,
                   maxevents)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_conn_parameters(min_interval, max_interval, latency, timeout):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x05
    payload = pack('<HHHH', min_interval, max_interval, latency, timeout)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_data_channel_classification(channel_map):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x19
    payload = pack('<B', len(channel_map)) + bytes(channel_map)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_discovery_timing(phys, scan_interval, scan_window):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x16
    payload = pack('<BHH', phys, scan_interval, scan_window)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_discovery_type(phys, scan_type):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x17
    payload = pack('<BB', phys, scan_type)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_privacy_mode(privacy, interval):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x0d
    payload = pack('<BB', privacy, interval)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def start_advertising(handle, discover, connect):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x14
    payload = pack('<BBB', handle, discover, connect)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def start_discovery(scanning_phy, mode):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x18
    payload = pack('<BB', scanning_phy, mode)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def stop_advertising(handle):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_GAP.value
    MSG_ID = 0x15
    payload = pack('<B', handle)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
