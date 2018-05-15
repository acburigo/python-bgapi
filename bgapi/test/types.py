from enum import IntEnum


class PacketType(IntEnum):
    PKT_PRBS9 = 0
    PKT_11110000 = 1
    PKT_10101010 = 2
    PKT_CARRIER_DEPRECATED = 3
    PKT_11111111 = 4
    PKT_00000000 = 5
    PKT_00001111 = 6
    PKT_01010101 = 7
    PKT_PN9 = 253
    PKT_CARRIER = 254


class Phy(IntEnum):
    PHY_1M = 1
    PHY_2M = 2
    PHY_125K = 3
    PHY_500K = 4
