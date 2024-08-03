import os
import binascii

secret_key = binascii.hexlify(os.urandom(24)).decode()
print(secret_key)
