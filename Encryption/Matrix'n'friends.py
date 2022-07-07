import numpy as np

suomi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def key_ceasar(alphabet):
    k = int(input('Value of k: '))
    word = input('Key word: ').lower()
    choice = input("(e)ncrypt or (d)ecrypt: ").lower()
    msg = input('Message to encrypt/decrypt: ').lower().split(" ")

    fixed_alphabet = []
    for letter in word:
        if letter not in fixed_alphabet:
            fixed_alphabet.append(letter)
            k += 1

    for letter in alphabet:
        if letter not in fixed_alphabet:
            fixed_alphabet.insert(k, letter)
            k += 1
        if k >= len(alphabet):
            k -= len(alphabet)
    
    if choice == "e":
        print(crypt_the_word(alphabet, fixed_alphabet, msg))
    elif choice == "d":
        print(crypt_the_word(fixed_alphabet, alphabet, msg))


def crypt_the_word(alphabet, fixed_alphabet, msg):
    crypt_msg = []
    for word in msg:
        crypt_wrd = []
        for letter in word:
            a = alphabet.index(letter)
            crypt_wrd.append(fixed_alphabet[a])
        x = "".join(crypt_wrd)
        crypt_msg.append(x)
    en_msg = " ".join(crypt_msg).upper()
    return en_msg
        

def vignere(alphabet):
    choice = input("(e)ncrypt or (d)ecrypt: ").lower()
    keyword = input('Key word: ')
    msg = input("Message to encrypt/decrypt: ").lower().replace(" ", "")
    msg = list(msg)

    keys = []
    split = 0
    for letter in keyword:
        keys.append(alphabet.index(letter))
        split += 1

    if choice == 'e':
        en_vig(alphabet, msg, keys, split)
    elif choice == 'd':
        de_vig(alphabet, msg, keys, split)

def en_vig(alphabet, msg, keys, split):
    split_msg = []
    while msg:
        for i in range(0, split):
            ltr = msg.pop(0)
            if ltr in alphabet:
                num = alphabet.index(ltr)
                nu_ltr = num + keys[i]
                if nu_ltr >= len(alphabet):
                    nu_ltr -= len(alphabet)
                split_msg.append(alphabet[nu_ltr])
                if not msg:
                    print("".join(split_msg).upper())
                    return


def de_vig(alphabet, msg, keys, split):
    split_msg = []
    while msg:
        for i in range(0, split):
            ltr = msg.pop(0)
            if ltr in alphabet:
                num = alphabet.index(ltr)
                nu_ltr = num - keys[i]
                if nu_ltr < 0:
                    nu_ltr += len(alphabet)
                split_msg.append(alphabet[nu_ltr])
                if not msg:
                    print("".join(split_msg).upper())
                    return

    
def count_inv_matrix(matrix, alphabet):
    a = matrix.tolist()
    num_a = matrix
    det = round((np.linalg.det(num_a)))
    while det < 0:
        det += len(alphabet)
    while det > len(alphabet):
        det -= len(alphabet)
    inv_number = solve_inverse_number(len(alphabet), det, alphabet)

    inv_matrix = [[], []]
    for k, line in enumerate(a):
        for i, number in enumerate(line):
            if k == 0 and i == 1 or k == 1 and i == 0:
                number = -number
            num = inv_number * number
            if k == 0 and i == 0:
                inv_matrix[1].insert(1, num)
            elif k == 1 and i == 1:
                inv_matrix[0].insert(0, num)
            elif k == 0 and i == 1:
                inv_matrix[0].insert(1, num)
            elif k == 1 and i == 0:
                inv_matrix[1].insert(0, num)

    for i, line in enumerate(inv_matrix):
        for a, number in enumerate(line):
            nu_nmbr = number
            while nu_nmbr < 0:
                nu_nmbr += len(alphabet)
            while nu_nmbr >= len(alphabet):
                nu_nmbr -= len(alphabet)
            inv_matrix[i][a] = nu_nmbr
    return inv_matrix


def solve_inverse_number(r0, x, alphabet):
    """solves the inverse number using euclidean algorithm"""
    qs = []
    while x > 0:
        r = int(r0 % x)
        q = int((r0 - r) / x)
        qs.append(q)
        r0 = x
        x = r
    inv_number = teet(qs, r0, alphabet)
    return inv_number


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
            i = i + 1


def matrix_crypt(alphabet):
    choice = input("(e)ncrypt or (d)ecrypt: ").lower()
    lena = len(alphabet)
    A = create_matrix('A')
    B = create_matrix('B')
    msg = input("Message to encrypt/decrypt: ").lower().replace(" ", "")

    if choice == "e":
        msg_matrix = create_word_matrix(msg, alphabet)
        C = A * msg_matrix + B
        open_matrix(C, lena, alphabet)
    
    elif choice == 'd':
        A = np.matrix(count_inv_matrix(A, alphabet))
        msg_matrix = create_word_matrix(msg, alphabet)
        C = A * msg_matrix + (-(A*B))
        open_matrix(C, lena, alphabet)



def open_matrix(C, lena, alphabet):
    C_list = C.tolist()
    for a, line in enumerate(C_list):
        for i, number in enumerate(line):
            if not 0 <= number < lena:
                while number < 0:
                    number += lena
                while number >= lena:
                    number -= lena
                C_list[a][i] = number
    
    crypted_msg = []
    k = 1
    for a, line in enumerate(C_list):
        for i, number in enumerate(line):
            if a == 0:
                crypted_msg.append(alphabet[number])
            else:
                i = k + i
                crypted_msg.insert(i, alphabet[number])
                k += 1
    print("".join(crypted_msg).upper())

            
def create_word_matrix(msg, alphabet):
    msg_matrix_u = []
    msg_matrix_l = []
    for i, letter in enumerate(msg):
        ltr_index = alphabet.index(letter)
        if i == 0:
            msg_matrix_u.append(ltr_index)
        elif i == 1:
            msg_matrix_l.append(ltr_index)
        elif i % 2 == 0:
            msg_matrix_u.append(ltr_index)
        else:
            msg_matrix_l.append(ltr_index)
    msg_matrix = np.matrix([msg_matrix_u, msg_matrix_l])
    return msg_matrix


def create_matrix(name):
    input1 = 1
    matrix_upper = []
    matrix_lower = []
    print('Give the upper values of matrix {} one at a time (blank to stop)'.format(name))
    while input1 != "":
        input1 = input('Value: ')
        if input1 != "":
            matrix_upper.append(int(input1))
    input1 = 1
    print('Give the lower values of the matrix {} one at a time (blank to stop)'.format(name))
    while input1 != "":
        input1 = input('Value: ')
        if input1 != "":
            matrix_lower.append(int(input1)) 
    matrix = np.matrix([matrix_upper, matrix_lower])
    return matrix



alphabet = input("(e)nglish or (f)innish: ").lower()
if alphabet == 'f':
    alphabet = suomi
    print('Finnish has been chosen.')
else:
    alphabet = english
    print('English has been chosen or set by default.')
print('Choose method, either (v)ignere, (k)ey Ceasar or (m)atrix.')
stop = 0
while stop == 0:
    choice = input()
    if choice == 'v':
        vignere(alphabet)
        stop = 1
    elif choice == 'k':
        key_ceasar(alphabet)
        stop = 1
    elif choice == 'm':
        matrix_crypt(alphabet)
        stop = 1
    else:
        print('Unregocnized command, choose either (v)ignere, (k)ey ceasar or (m)atrix')