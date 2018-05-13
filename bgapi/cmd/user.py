from struct import pack

from bgapi.cmd import command


def message_to_target(data):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = 0xff
    MSG_ID = 0x00
    payload = pack('<B', len(data)) + data
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
