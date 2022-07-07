def solve_key(ciphertext, plaintext):
    key = ciphertext ^ plaintext
    return key

ciphers = (0b01101001, 0b00010101, 0x5f, 0x4e, 0x20, 0x1c, 0xad, 0x61)
letters = ('Hi Kimmo')
letters2 = ('No Rauli')

my_word = ('Vitonen!')
my_cipher = []

keys = []
for i in range(len(ciphers)):
    key = solve_key(ciphers[i], ord(letters[i]))
    keys.append(key)


ciphers = []
for i in range(len(letters2)):
    cipher = solve_key(keys[i], ord(letters2[i]))
    ciphers.append(cipher)


for i in range(len(letters2)):
    print(chr(ciphers[i]), end='')
print('')

for i in range(len(letters2)):
    print(chr(ciphers[i]^keys[i]), end='')

for i in range(8):
    cipher = solve_key(keys[i], ord(my_word[i]))
    my_cipher.append(cipher)
print()

for i in range(8):
    print(chr(my_cipher[i]), end='')
print()
