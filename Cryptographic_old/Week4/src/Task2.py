import hashlib
import time
import sys
import random
import string

alphabet = "abcdefghijklmnopqrstuvwxyz"

hashes = {}
msgs = {}

def generate_msg(old=None):
    if not old:
        msg = 'a'
    else:
        msg = list(old)
        if old[-1] != 'z':
            msg[-1] = alphabet[alphabet.index(old[-1])+1]
        else:
            i = -1
            try:
                while old[i] == 'z':
                    msg[i] = 'a'
                    i -= 1
                msg[i] = alphabet[alphabet.index(old[i])+1]
            except IndexError:
                msg = 'a'
                for i in range(len(old)):
                    msg = msg + 'a'
    return ''.join(msg)


def generate_random_msg(n=1):
    msg = ''
    while True:
        msg = msg + random.choice(string.printable)
        if msg not in msgs:
            msgs[msg] = msg
            return msg
        

def task_2_1():
    time1 = time.perf_counter()
    for i in range(0, 10000000):
        msg = generate_random_msg()
        if i % 10000 == 0:
            print(i)
            print(msg)
        test_hash = hashlib.md5(msg.encode())
        hash_numbers = test_hash.hexdigest()
        for value in hashes:
            if list(hash_numbers)[:8] == list(hashes[value])[:8]:
                print(msg, test_hash.hexdigest())
                print(value, hashes[value])
                print(time.perf_counter() - time1)
                sys.exit()
        hashes[msg] = hash_numbers
        


def task_2_2():
    time1 = time.perf_counter()
    msg = generate_random_msg()
    for i in range(100000000):
        if i % 1000000 == 0:
            print(i)
            print(msg)
        test_hash = hashlib.md5(msg.encode())
        hash_ = test_hash.hexdigest()
        if hash_[:6] == '000000':
            print(msg, hash_)
            print(time.perf_counter()-time1)
            sys.exit()
        msg = generate_random_msg()

task_2_2()