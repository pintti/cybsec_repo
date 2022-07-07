from Cryptodome.Cipher import AES
import base64
import random
import string
import sys
import time

msgs = {}

key = b'this is a16B key'
nonce = b'nonkense'
data1 = b'this is the first message'

def generate_random_msg():
    msg = ''
    while True:
        msg = msg + random.choice(string.printable)
        if msg not in msgs:
            msgs[msg] = msg
            return msg

def generate_random_len_msg(n):
    msg = ''
    while len(msg) != n:
        msg = msg + random.choice(string.printable)
    return msg

def task_1():
    nonce = bytes(generate_random_len_msg(7).encode('utf-8'))
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce, mac_len=4)
    _, tag = cipher.encrypt_and_digest(data1)
    msg = ''
    new_tag = ''
    time1 = time.time()
    for i in range(1000000000):
        if i % 100000 == 0:
            pass
            #print(msg, list(new_tag))
        msg = generate_random_msg()
        cipher2 = AES.new(key, AES.MODE_GCM, nonce=nonce, mac_len=4)
        _, new_tag = cipher2.encrypt_and_digest(bytes(msg.encode('utf-8')))
        if list(new_tag)[:2] == list(tag)[:2]:
            #print(list(new_tag), list(tag))
            #print('Old tag:', base64.b64encode(tag).decode('utf-8'), ' New msg:', msg, ' New tag:', base64.b64encode(new_tag).decode('utf-8'))
            #print('Time', time.time()-time1)
            return time.time()-time1

times = []
time_sum = 0
for i in range(20):
    times.append(task_1())
for time in times:
    time_sum = time_sum + time
time_sum = time_sum/len(times)
print(time_sum)
    