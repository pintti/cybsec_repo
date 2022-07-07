from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

key = get_random_bytes(4)
print(key)
cipher = AES.new(key, AES.MODE_EAX)
print(cipher)