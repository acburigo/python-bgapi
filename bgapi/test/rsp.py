from bgapi.base import _parse_basic_response


def _dtm_end(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _dtm_rx(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _dtm_tx(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)
