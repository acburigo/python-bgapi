from enum import (IntEnum, IntFlag)


class BondingKey(IntFlag):
    LTK = 1
    ADDR_PUBLIC = 2
    ADDR_STATIC = 4
    IRK = 8
    EDIVRAND = 16
    CSRK = 32
    MASTERID = 64


class IoCapability(IntEnum):
    DISPLAYONLY = 0
    DISPLAYYESNO = 1
    KEYBOARDONLY = 2
    NOINPUTNOOUTPUT = 3
    KEYBOARDDISPLAY = 4
