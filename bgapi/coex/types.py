from enum import IntFlag


class Option(IntFlag):
    OPTION_ENABLE = 256
    OPTION_TX_ABORT = 1024
    OPTION_HIGH_PRIORITY = 2048
