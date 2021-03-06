from enum import (IntEnum, IntFlag)


class AttOpcode(IntEnum):
    READ_BY_TYPE_REQUEST = 8
    READ_BY_TYPE_RESPONSE = 9
    READ_REQUEST = 10
    READ_RESPONSE = 11
    READ_BLOB_REQUEST = 12
    READ_BLOB_RESPONSE = 13
    READ_MULTIPLE_REQUEST = 14
    READ_MULTIPLE_RESPONSE = 15
    WRITE_REQUEST = 18
    WRITE_RESPONSE = 19
    WRITE_COMMAND = 82
    PREPARE_WRITE_REQUEST = 22
    PREPARE_WRITE_RESPONSE = 23
    EXECUTE_WRITE_REQUEST = 24
    EXECUTE_WRITE_RESPONSE = 25
    HANDLE_VALUE_NOTIFICATION = 27
    HANDLE_VALUE_INDICATION = 29


class ClientConfigFlag(IntFlag):
    DISABLE = 0
    NOTIFICATION = 1
    INDICATION = 2


class ExecuteWriteFlag(IntFlag):
    CANCEL = 0
    COMMIT = 1
