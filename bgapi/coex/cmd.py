from struct import pack

from bgapi import command


def get_counters(reset):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x03
    MSG_CLASS = 0x20
    MSG_ID = 0x01
    payload = pack('<B', reset)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_options(mask, options):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x08
    MSG_CLASS = 0x20
    MSG_ID = 0x00
    payload = pack('<II', mask, options)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
