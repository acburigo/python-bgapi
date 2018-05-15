from bgapi.base import _parse_basic_response


def _flash_set_address(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _flash_upload(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)


def _flash_upload_finish(data: bytes, offset: int = 0):
    return _parse_basic_response(data, offset)
