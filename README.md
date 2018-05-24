# Python BGAPI
This is a library for creating and parsing BGAPI packets.

**This library is under construction.**

## Supported Python Versions
This library currently supports **Python 3.6** and possibly latter versions.

## Supported API Versions
This library currently supports **Silicon Labs Bluetooth Software API version 2.8.1** (non-deprecated only).

## Usage

### Create binary package:

```
In [1]: import bgapi

In [2]: bgapi.system.cmd.reset(0)
Out[2]: b' \x01\x01\x01\x00'
```

### Parse binary packet:

```
In [1]: import bgapi

In [2]: data = b'\xa0\x12\x01\x00\x02\x00\x08\x00\x01\x00\xc2\x00\x00\x00\x05\x01\x01\x00\x99\x07\x9cx'

In [3]: len(data)
Out[3]: 22

In [4]: packet, offset = bgapi.from_binary(data)

In [5]: offset
Out[5]: 22

In [6]: packet
Out[6]:
{'msg_type': 160,
 'min_payload_len': 18,
 'msg_class': 1,
 'msg_id': 0,
 'payload': {'major': 2,
  'minor': 8,
  'patch': 1,
  'build': 194,
  'bootloader': 17104896,
  'hw': 1,
  'hash': 2023491481}}
```

## Installation

We are not in PyPI yet.

If you are interested in the latest (possibly unstable) features, you may issue the following command:

`pip install --upgrade git+https://github.com/acburigo/python-bgapi.git`

## Developers

This repository is currently maintained by [Arthur Crippa Búrigo](https://github.com/acburigo).
