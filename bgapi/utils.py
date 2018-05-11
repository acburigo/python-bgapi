from struct import pack

def uuid_to_bytes(uuid):
    return pack('<' + str(len(uuid)) + 'B', uuid)


def characteristic_list_to_bytes(characteristic_list):
    return pack('<' + str(len(characteristic_list)) + 'H', *characteristic_list)
