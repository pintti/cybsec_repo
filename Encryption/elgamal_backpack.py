from string import ascii_lowercase, ascii_uppercase
from primitive_root_and_DH_key import *


def magic(num, mod):
    if num == 0:
        return (mod, 0, 1)
    else:
        left, y, x = magic(mod % num, num)
        return (left, x - (mod // num) * y, y)


def invmod(x, mod):
    """Method for getting the inverse modulo number."""
    left, x, y = magic(x, mod)
    if left != 1:
        raise Exception("NO MODULAR POSSIBLE")
    else:
        return x % mod


def encrypt_backpack(super_queue: list[int], mod: int, ab: int, string: str):
    encrypt_list = []
    public_queue = super_queue #get_public_queue(super_queue, ab, mod)
    string_list = get_string_list(string)
    for string in string_list:
        enc_num = 0
        for i, num in enumerate(string):
            if num == "1":
                enc_num += public_queue[i]
        encrypt_list.append(enc_num)
    return encrypt_list


def decrypt_backpack(super_queue: list[int], mod: int, ab: int, encrypt_list: list[int]):
    decrypt_list = []
    bb = invmod(ab, mod)
    for num in encrypt_list:
        dec_num = num * bb % mod
        print(dec_num)
        decrypt_list.append(get_binary_num_from_num(super_queue, dec_num))
    return decrypt_list


def get_binary_num_from_num(super_queue: list[int], num: int):
    binary_list = [16, 8, 4, 2, 1]
    binary_num = 0
    i = len(super_queue)-1
    while(num > 0):
        if num >= super_queue[i]:
            binary_num += binary_list[i]
            num -= super_queue[i]
        i -= 1
    return binary_num


def get_string_list(string: str):
    string_list = []
    for letter in string:
        binary = bin(ascii_lowercase.index(letter)).removeprefix("0b")
        if len(binary) < 5:
            binary = ("0" * (5 - len(binary))) + binary
        string_list.append(binary)
    return string_list


def get_public_queue(super_queue: list[int], ab: int, mod: int):
    public_queue = []
    for num in super_queue:
        public_queue.append(num * ab % mod)
    return public_queue

super_queue = [3, 4, 8, 16, 32]
mod = 79
ab = 11
#string = "hi"
#encrypt_list = encrypt_backpack(super_queue, mod, ab, string)
#print(encrypt_list)
print(decrypt_backpack(super_queue, mod, ab, [27, 71]))
print(ascii_lowercase[6], ascii_lowercase[14])


"""
m1 = 72
mod = 113
group = 101
a = 10

public_a = 22 #get_public_key(a, group, mod)
public_b = 64 #get_public_key(23, group, mod)
together = get_together_key(public_b, a, mod)
print(public_a, public_b, together)

secret_msg = 108 #m1 * together % mod
#print(secret_msg)

inverse = invmod(together, mod)
print(inverse)
decrypt_msg = secret_msg * inverse % mod
print(decrypt_msg)

secret_msg2 = 47
real_msg = 42
decrypt_earlier_secret = secret_msg * invmod(secret_msg2, mod) * real_msg % mod
print(decrypt_earlier_secret)
"""