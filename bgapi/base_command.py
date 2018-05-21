from struct import pack


def command(msg_type, min_payload_length, msg_class, msg_id, payload=b''):
    b = pack('<BBBB', msg_type, len(payload), msg_class, msg_id)
    b += payload
    return b
