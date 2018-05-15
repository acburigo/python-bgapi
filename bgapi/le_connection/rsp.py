from bgapi.base import _parse_basic_response


def _close(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _disable_slave_latency(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _get_rssi(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_parameters(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_phy(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)
