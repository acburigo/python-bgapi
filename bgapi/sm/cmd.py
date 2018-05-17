from struct import pack

from bgapi import command
from bgapi.types import (MessageType, MessageClass)


def bonding_confirm(connection, confirm):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x0e
    payload = pack('<BB', connection, confirm)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def configure(flags, io_capabilities):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x01
    payload = pack('<BB', flags, io_capabilities)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def delete_bonding(bonding):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x06
    payload = pack('<B', bonding)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def delete_bondings():
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x07
    payload = b''
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def enter_passkey(connection, passkey):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x05
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x08
    payload = pack('<Bi', connection, passkey)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def increase_security(connection):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x04
    payload = pack('<B', connection)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def list_all_bondings():
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x0b
    payload = b''
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def passkey_confirm(connection, confirm):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x09
    payload = pack('<BB', connection, confirm)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_bondable_mode(bondable):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x00
    payload = pack('<B', bondable)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_debug_mode():
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x00
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x0f
    payload = b''
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_oob_data(oob_data):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x0a
    payload = pack('<B', len(oob_data)) + oob_data
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_passkey(passkey):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x04
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x10
    payload = pack('<i', passkey)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def set_sc_remote_oob_data(oob_data):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x12
    payload = pack('<B', len(oob_data)) + oob_data
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def store_bonding_configuration(max_bonding_count, policy_flags):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x02
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x02
    payload = pack('<BB', max_bonding_count, policy_flags)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)


def use_sc_oob(enable):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MIN_PAYLOAD_LENGTH = 0x01
    MSG_CLASS = MessageClass.SM.value
    MSG_ID = 0x11
    payload = pack('<B', enable)
    return command(MSG_TYPE, MIN_PAYLOAD_LENGTH, MSG_CLASS, MSG_ID, payload)
