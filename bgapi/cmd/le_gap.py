from struct import pack

from bgapi.cmd import command
from bgapi.utils import address_to_bytes


def bt5_set_adv_data(handle, scan_rsp, adv_data):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x03
    MSG_CLASS = 0x03
    MSG_ID = 0x0c
    payload = pack('<BBB', handle, scan_rsp, len(adv_data)) + adv_data
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def clear_advertise_configuration(handle, configurations):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x05
    MSG_CLASS = 0x03
    MSG_ID = 0x13
    payload = pack('<BI', handle, configurations)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def connect(address, address_type, initiating_phy):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x08
    MSG_CLASS = 0x03
    MSG_ID = 0x1a
    payload = address_to_bytes(address) + pack('<BB', address_type,
                                               initiating_phy)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def end_procedure():
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = 0x03
    MSG_ID = 0x03
    payload = b''
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_advertise_channel_map(handle, channel_map):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x03
    MSG_ID = 0x0f
    payload = pack('<BB', handle, channel_map)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_advertise_configuration(handle, configurations):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x05
    MSG_CLASS = 0x03
    MSG_ID = 0x12
    payload = pack('<BI', handle, configurations)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_advertise_phy(handle, primary_phy, secondary_phy):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x03
    MSG_CLASS = 0x03
    MSG_ID = 0x11
    payload = pack('<BBB', handle, primary_phy, secondary_phy)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_advertise_report_scan_request(handle, report_scan_req):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x03
    MSG_ID = 0x10
    payload = pack('<BB', handle, report_scan_req)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_advertise_timing(handle, interval_min, interval_max, duration, maxevents):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x0c
    MSG_CLASS = 0x03
    MSG_ID = 0x0e
    payload = pack('<BIIHB', handle, interval_min, interval_max, duration, maxevents)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_conn_parameters(min_interval, max_interval, latency, timeout):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x08
    MSG_CLASS = 0x03
    MSG_ID = 0x05
    payload = pack('<HHHH', min_interval, max_interval, latency, timeout)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
