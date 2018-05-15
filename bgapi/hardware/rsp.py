from bgapi.base import _parse_basic_response


def _set_lazy_soft_timer(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _set_soft_timer(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)
