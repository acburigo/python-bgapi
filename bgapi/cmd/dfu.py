from struct import pack

from bgapi.cmd import command


def flash_set_address(address):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = 0x00
    MSG_ID = 0x01
    payload = pack('<I', address)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def flash_upload(data):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = 0x00
    MSG_ID = 0x02
    payload = data
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def flash_upload_finish():
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = 0x00
    MSG_ID = 0x03
    payload = b''
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def reset(dfu):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = 0x00
    MSG_ID = 0x00
    payload = pack('<B', dfu)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
