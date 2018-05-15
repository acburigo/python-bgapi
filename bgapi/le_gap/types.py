from enum import (IntEnum, IntFlag)


class AddressType(IntEnum):
    PUBLIC = 0
    RANDOM = 1
    PUBLIC_IDENTITY = 2
    RANDOM_IDENTITY = 3


class AdvAddressType(IntEnum):
    IDENTITY_ADDRESS = 0
    NON_RESOLVABLE = 1


class ConnectableMode(IntEnum):
    NON_CONNECTABLE = 0
    DIRECTED_CONNECTABLE = 1
    CONNECTABLE_SCANNABLE = 2
    SCANNABLE_NON_CONNECTABLE = 3
    CONNECTABLE_NON_SCANNABLE = 4


class DiscoverMode(IntEnum):
    LIMITED = 0
    GENERIC = 1
    OBSERVATION = 2


class DiscoverableMode(IntEnum):
    NON_DISCOVERABLE = 0
    LIMITED_DISCOVERABLE = 1
    GENERAL_DISCOVERABLE = 2
    BROADCAST = 3
    USER_DATA = 4


class PhyType(IntFlag):
    PHY_1M = 1
    PHY_2M = 2
    PHY_CODED = 4
