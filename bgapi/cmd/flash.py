from struct import pack

from bgapi.cmd import cmd


def ps_erase(key):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x0d
    MSG_ID = 0x04
    payload = pack('<H', key)
    return cmd(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def ps_erase_all():
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = 0x0d
    MSG_ID = 0x01
    payload = b''
    return cmd(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def ps_load(key):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = 0x0d
    MSG_ID = 0x03
    payload = pack('<H', key)
    return cmd(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def ps_save(key, value):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x03
    MSG_CLASS = 0x0d
    MSG_ID = 0x02
    payload = pack('<H', key) + value
    return cmd(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
