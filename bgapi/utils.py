from struct import pack


def address_to_bytes(address):
    address = address.replace(':', '')
    address = bytes.fromhex(address)[::-1]
    return pack('<' + str(len(address)) + 'B', address)


def uuid_to_bytes(uuid):
    return pack('<' + str(len(uuid)) + 'B', uuid)


def characteristic_list_to_bytes(characteristic_list):
    return pack('<' + str(len(characteristic_list)) + 'H', *characteristic_list)
