suomi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def teet(qs, t2, z):
    t1 = 0
    i = 0
    t = 0
    while t < z:
        t = t1 - (qs[i] * t2)
        if t == z or -t == z:
            return t2
        else:
            t1 = t2
            t2 = t
            i = i + 1


def solve_inverse_number(r0, x):
    """solves the inverse number using euclidean algorithm"""
    qs = []
    r_og = r0
    while x > 0:
        r = int(r0 % x)
        q = int((r0 - r) / x)
        qs.append(q)
        r0 = x
        x = r
    inv_number = teet(qs, r0, r_og)
    return inv_number


def solve_starting_number(a_length, z):
    k = 0
    M = a_length - 1
    while M < z:
        k += 1
        M += (a_length - 1) * 10**(2*k)
    return k


def turn_word_to_numbers(word, alphabet, k):
    i = 0
    number_list = []
    while i < len(word):
        number = 0
        for p in range(i, i+k):
            number += alphabet.index(word[p]) * 10**(2*((i+k)-p-1))
        number_list.append(number)
        i += k
    return number_list


def affini_letter_change(a, b, ln):
    return a * ln + b


def count_number_down(number, z):
    while number > z:
        number -= z
    return number


def turn_number_to_word(alphabet, lista, k):
    word = []
    for numbers in lista:
        for i in range(k):
            number = int(numbers[i*2]) * 10
            number += int(numbers[i*2+1]) - 1
            while number >= len(alphabet):
                number -= len(alphabet)
            word.append(alphabet[number])
    return word


def slice_ecnrypt_method(alphabet, word, z, a, b):
    k = solve_starting_number(len(alphabet), z)
    number_list = turn_word_to_numbers(word, alphabet, k)
    print(number_list)
    for i, number in enumerate(number_list):
        nu_number = count_number_down(affini_letter_change(a, b, number), z)
        number_list[i] = str(nu_number).zfill(k*2)
    nu_word = turn_number_to_word(alphabet, number_list, k)
    print(number_list)
    print(nu_word)
    

def solve_starting_k(a_length,z):
    k = 0
    m = 0
    while m < z:
        k += 1
        m = a_length**k
    return k - 1


def fill_numbers(lista, k):
    i = 0
    for number in lista:
        lista[i] = str(number).zfill(k*2)
        i += 1
    return lista


def count_together(lista, a_length, k):
    number_list = []
    for numbers in lista:
        number = 0
        add = 0
        p = k - 1
        for i in range(k):
            add = int(numbers[i*2]) * 10
            add += int(numbers[i*2+1])
            number += add * a_length**p
            p -= 1
        number_list.append(number)
    return number_list


def lenghten_word(word, k):
    while len(word) % k != 0:
        word = word + 'a'
    return word

            
def basis_encrypt_method(alphabet, word, z, a, b):
    k = solve_starting_k(len(alphabet), z)
    print(k)
    if len(word) % k != 0:
        word = lenghten_word(word, k)
    ltr_numbers = fill_numbers(turn_word_to_numbers(word, alphabet, k), k)
    numbers = count_together(ltr_numbers, len(alphabet), k)
    print(numbers)
    numbers = count_new_numbers(numbers, z, a, b)
    print(numbers)
    print(turn_to_letters(numbers, alphabet, k))
    

def count_new_numbers(lista, z, a, b):
    i = 0
    for number in lista:
        number = affini_letter_change(a, b, number)
        number = count_number_down(number, z)
        lista[i] = number
        i += 1
    return lista


def turn_to_letters(lista, alphabet, k):
    word_list = []
    for check in lista:
        number = 0
        p = k
        i = len(alphabet)
        while number != check:
            nu_number = i * len(alphabet)**p
            if (number + nu_number) > check:
                i -= 1
                nu_number = number
            else:
                number += nu_number
                word_list.append(alphabet[i])
                p -= 1
                i = len(alphabet)
    return word_list
            



basis_encrypt_method(english, 'supernatural', 682103, 329, 0)