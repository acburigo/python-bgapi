from bgapi.base import _parse_result


def _dtm_end(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _dtm_rx(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset


def _dtm_tx(data: bytes, offset: int = 0):
    result, offset = _parse_result(data, offset)
    payload = {'result': result}
    return payload, offset
