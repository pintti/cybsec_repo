suomi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(alphabet):
    k = int(input('Please give the encryption key (k): '))
    message = input('Please give the message to encrypt: ').lower().split(" ")
    en_message = []
    for word in message:
        encrypted = []
        for letter in word:
            if letter in alphabet:
                index = alphabet.index(letter)
                encoded = index + k
                if encoded >= len(alphabet):
                    encoded = encoded - len(alphabet)
                enletter = alphabet[encoded]
                encrypted.append(enletter)
            encryptword = "".join(encrypted).strip(" ")
    print(encryptword)

def decrypt(alphabet):
    k = int(input('Please give the decryption key (k): '))
    message = input('Please give the encrypted message: ').lower().split(" ")
    de_message = []
    for word in message:
        decrypted = []
        for letter in word:
            if letter in alphabet:
                index = alphabet.index(letter)
                decoded = index - k
                if decoded < 0:
                    decoded = decoded + len(alphabet)
                enword = alphabet[decoded]
                decrypted.append(enword)
            decryptword = "".join(decrypted).strip(" ")
    print(decryptword)


def m_encrypt(alphabet):
    x = int(input('Please give the encryption key (x): '))
    message = input('Please give the message to encrypt: ').lower().split(" ")
    en_message = []
    for word in message:
        encrypted = []
        for letter in word:
            if letter in alphabet:
                index = alphabet.index(letter)
                encoded = index * x
                while encoded >= len(alphabet):
                    encoded = encoded - len(alphabet)
                encrypted.append(alphabet[encoded])
            encryptionword = "".join(encrypted).strip(" ")
    print(encryptionword)


def m_decrypt(alphabet):
    denumber = 0
    r0 = len(alphabet)
    x = int(input('Please give the key: '))
    message = input('Please give the encrypted message: ').lower().split(" ")
    qs = []
    de_message = []
    while x > 0:
        r = int(r0 % x)
        q = int((r0 - r) / x)
        qs.append(q)
        r0 = x
        x = r
    denumber = teet(qs, r0)
    if denumber < 0:
            denumber = denumber + len(alphabet)
    for word in message:
        decrypted = []
        for letter in word:
            if letter in alphabet:
                index = alphabet.index(letter)
                decoded = index * denumber
                while decoded > len(alphabet):
                    decoded = decoded - len(alphabet)
                decrypted.append(alphabet[decoded])
            decryptionword = "".join(decrypted).strip(" ")
    print(decryptionword)


def teet(qs, t2):
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
            i = i + 1


language = input('Choose either (f)innish or (e)nglish: ')
alphabet = english
if language == 'f':
    alphabet = suomi
elif language == 'e':
    alphabet = english
else:
    print('English has been chosen by default')
choice = input('Choose either (d)ecrypt or (e)ncrypt: ')
if choice == 'e':
    way = input('(s)um or (m)ultiplication: ')
    if way == 's':
        encrypt(alphabet)
    elif way == 'm':
        m_encrypt(alphabet)
elif choice == 'd':
    way = input('(s)um or (m)ultiplication: ')
    if way == 's':
        decrypt(alphabet)
    elif way == 'm':
        m_decrypt(alphabet)
else:
    print('No function selected, terminating')
input()