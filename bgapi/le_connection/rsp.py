from bgapi.base import _parse_result


def _close(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _disable_slave_latency(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _get_rssi(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _set_parameters(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _set_phy(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset
