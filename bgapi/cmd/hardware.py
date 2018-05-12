from struct import pack

from bgapi.cmd import command


def set_lazy_soft_timer(time, slack, handle, single_shot):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x0a
    MSG_CLASS = 0x0c
    MSG_ID = 0x0c
    payload = pack('<IIBB', time, slack, handle, single_shot)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_soft_timer(time, handle, single_shot):
    MSG_TYPE = 0x20
    MIN_PAYLOAD_LENGTH = 0x06
    MSG_CLASS = 0x0c
    MSG_ID = 0x00
    payload = pack('<IBB', time, handle, single_shot)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
