from Cryptodome.Cipher import ChaCha20
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from base64 import b64encode, b64decode
import json
import time

plaintext = b"Move the tables to the patio as soon as possible!"
plaintext2 = b"Move the chairs to the house as soon as possible!"
plaintext_mine_1 = b'Man, I could really go for a beer right now.'
plaintext_mine_2 = b'Men, I could really go for a beer right now.'
key = b'I dont know what I am doing mano'
key2 = b'I dont know what I am doing mana'
nonce = b'disnonce'

def read_text(msg):
    text = [chr(number) for number in list(msg)]
    return "".join(text)

def task_1_1():
    cipher_en = ChaCha20.new(key=key, nonce=nonce)
    cipher_de = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher_en.encrypt(plaintext)
    print("Ciphertext:", list(ciphertext))

    keystream = [(a ^ b) for a,b in zip(ciphertext, plaintext)]
    print("Keystream:", keystream)

    ciphertext2 = [(a ^ b) for a,b in zip(keystream, plaintext2)]
    print("Ciphertext2:", ciphertext2)

    print(read_text(ciphertext))
    print(read_text(ciphertext2))

    print(cipher_de.decrypt(bytes(ciphertext2)))

def task_1_2():
    cipher_en_1 = ChaCha20.new(key=key, nonce=nonce)
    cipher_en_2 = ChaCha20.new(key=key2, nonce=nonce)
    ciphertext1 = cipher_en_1.encrypt(plaintext_mine_1)
    ciphertext2 = cipher_en_2.encrypt(plaintext_mine_2)

    print("Cipher1:", read_text(ciphertext1))
    print("Cipher2:", read_text(ciphertext2))

    print("Cipher1:", list(ciphertext1))
    print("Cipher2:", list(ciphertext2))

def task_1_3():
    for i in range(3):
        time1 = time.perf_counter()
        if i == 0:
            cipher = AES.new(key, AES.MODE_CBC)
            cipher.encrypt(pad(plaintext, AES.block_size))
        if i == 1:
            cipher = AES.new(key, AES.MODE_CTR)
            cipher.encrypt(plaintext)
        if i == 2:
            cipher = ChaCha20.new(key=key)
            cipher.encrypt(plaintext)
        time2 = time.perf_counter()
        print(i, time2-time1)