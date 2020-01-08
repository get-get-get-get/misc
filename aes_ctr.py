#!/usr/bin/env python3
import binascii
import Crypto           # pycryptodome
import os
import struct

# Generate key
k = os.urandom(16)
print("key: {k}")

# Pick starting value for counter
nonce = struct.unpack('<Q', os.urandom(8))[0]
# Instantiate counter function
ctr = Crypto.Util.Counter.new(128, initial_value=nonce)
# Instantiate AES in CTR mode
aes = Crypto.Cipher.AES.new(k, Crypto.Cipher.AES.MODE_CTR, counter=ctr)

# Encrypt some plaintext
p = b'\x00\x01\x02\x03'
c = aes.encrypt(p)
print(f"enc({binascii.hexlify(p)} = {binascii.hexlify(c)})")