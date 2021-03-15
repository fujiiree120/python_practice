"""
from Crypto.Cipher import  AES
import string
import random

key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
print(key)
"""

import hashlib

user_name = 'user1'
user_password = 'password'
db = {}
password = bytes(user_password, 'UTF-8')
digest = hashlib.sha256(password).hexdigest()
db[user_name] = digest

print(db)
