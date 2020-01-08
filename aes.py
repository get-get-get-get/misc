#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii
import os

'''
from "Serious Cryptography"
'''

# Pick a random 16-byte key
k = os.urandom(16)
print(f"k = {binascii.hexlify(k)}")

# Create AES-128 instance to encrypt a block
cipher = Cipher(algorithms.AES(k), modes.ECB(), backend=default_backend())
aes_encrypt = cipher.encryptor()
aes_decrypt = cipher.decryptor()

# Set plaintext block p to all-zero string
p = b"\x00" * 16
print(f"p = {p}")

# Encrypt plaintext p to ciphertext c
c = aes_encrypt.update(p) + aes_encrypt.finalize()
print(f"enc({binascii.hexlify(p)}) = {binascii.hexlify(c)}")

# Decrypt ciphertext c to plaintext p
p = aes_decrypt.update(c) + aes_decrypt.finalize()
print(f"dec({binascii.hexlify(c)}) = {binascii.hexlify(p)}")
