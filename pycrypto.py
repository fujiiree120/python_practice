from Crypto.Cipher import  AES
import string
import random

key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
print(key)

