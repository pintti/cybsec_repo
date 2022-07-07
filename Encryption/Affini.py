suomi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def affini_encrypt(alphabet):
    a = int(input('Value of key a: '))
    b = int(input('Value of key b: '))
    msg = input('Message to encrypt: ').lower().split(" ")
    encrypt_msg = []
    encrypted = []
    for word in msg:
        for letter in word:
            if letter in alphabet:
                index = alphabet.index(letter)
                encrypt = a * index + b
                while encrypt >= len(alphabet):
                    encrypt = encrypt - len(alphabet)
                enletter = alphabet[encrypt]
                encrypted.append(enletter)
            encrypt_wrd = "".join(encrypted)
    print(encrypt_wrd)


def affini_decrypt(alphabet):
    a = int(input('Value of key a: '))
    b = int(input('Value of key b: '))
    msg = input('Message to decrypt: ').lower().split(" ")
    qs = []
    r0 = len(alphabet)
    while a > 0:
        r = int(r0 % a)
        q = int((r0 - r) / a)
        qs.append(q)
        r0 = a
        a = r
    inv_number = teet(qs, r0, alphabet)
    if inv_number < 0:
        inv_number = inv_number + len(alphabet)
    b = -b + len(alphabet)
    b = b * inv_number
    while b > len(alphabet):
        b = b - len(alphabet)
    decrypt_msg = []
    decrypted = []
    for word in msg:
        for letter in word:
            if letter in alphabet:
                index = alphabet.index(letter)
                decrypt = index * inv_number + b
                while decrypt >= len(alphabet):
                    decrypt = decrypt - len(alphabet)
                decrypted.append(alphabet[decrypt])
            decrypt_wrd = "".join(decrypted)
    print(decrypt_wrd)

    
def teet(qs, t2, alphabet):
    t1 = 0
    i = 0
    t = 0
    while t < len(alphabet):
        t = t1 - (qs[i] * t2)
        if t == len(alphabet) or -t == len(alphabet):
            return t2
        else:
            t1 = t2
            t2 = t
            i += 1


language = input('Choose either (f)innish or (e)nglish alphabet: ')
alphabet = english
if language == 'f':
    alphabet = suomi
elif language == 'e':
    alphabet = english
else:
    print('English has been chosen by default')
choice = input('Choose either (d)ecrypt or (e)ncrypt: ')
if choice == 'e':
    affini_encrypt(alphabet)
elif choice == 'd':
    affini_decrypt(alphabet)
else:
    print('No function selected, terminating')
input()