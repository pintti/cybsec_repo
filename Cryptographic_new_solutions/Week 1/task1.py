encoded_message = "Hi Kimmo"
ciphers = (0x69, 0x15, 0x5f, 0x4e, 0x20, 0x1c, 0xad, 0x61)
rauli_message = "No Rauli"

chosen_message = "Ykkönen?"


def XOR(letter1, letter2):
    return letter1 ^ letter2 

def solve_keys():
    keys = []
    for i in range(len(ciphers)):
        keys.append(XOR(ciphers[i], ord(encoded_message[i])))
        print(hex(keys[i]))
    return keys

def task_point_one(keys, msg):
    encrypted_msg = ""
    for i in range(len(keys)):
        encrypted_msg += chr(XOR(keys[i], ord(msg[i])))
    print(encrypted_msg)

def task_point_two(keys, msg):
    cipher = [chr(XOR(ord(chosen_message[i]), keys[i])) for i in range(len(keys))]
    print(cipher)

keys = solve_keys()
task_point_one(keys, rauli_message)
task_point_two(keys, chosen_message)
