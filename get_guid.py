#!/usr/bin/env python3

import struct
import hashlib
import sys
import os
import binascii

if len(sys.argv) != 2:
    print("usage: get_guid.py <provider-name>")
    exit(1)

providerName = sys.argv[1]

providerNameBytes = bytearray(providerName.upper().encode("utf-16BE"))

namespace = bytearray(b'\x48\x2C\x2D\xB2\xC3\x90\x47\xC8\x87\xF8\x1A\x15\xBF\xC1\x30\xFB')

output = hashlib.sha1(namespace + providerNameBytes)

output = output.hexdigest()

print(
    output[6:8] + output[4:6] + output[2:4] + output[0:2] + "-" + \
    output[10:12] + output[8:10] + "-" + \
    "5" + output[15:16] + output[12:14] + "-" + \
    output[16:20] + "-" + \
    output[20:32]
)



# 5e50de03-107c-5a83-74c6-998c4491e7e9