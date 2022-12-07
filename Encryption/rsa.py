finnish = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


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


def get_between(num, mod):
    while(num < 0):
        num += mod
    while(num > mod):
        num = num % mod
    return num


def get_cipher_nums(plain_nums: list[int], e: int, n: int):
    """args: 
    plain_nums: list of plain numbers to be ciphered.
    e: exponent to raise the plain numbers to
    n: the number to divide the exponential numbers by"""
    cipher_nums = []
    for number in plain_nums:
        cipher_nums.append(get_between(number**e, n))
    return cipher_nums


def get_plain_nums(plaintext: str, style: str):
    """args:
    plaintext: a string to be numbered into
    style: finnish or english style"""
    plain_nums = []
    for letter in plaintext:
        if style == "fi":
            plain_nums.append(finnish.index(letter))
        elif style == "en":
            plain_nums.append(english.index(letter))
    return plain_nums


def turn_nums_into_num(cipher_nums: list[int]):
    """args:
    cipher_nums: a list of cipher nums"""
    len_str = len(cipher_nums)
    number = 0
    k = 0
    for i in range(1, len_str):
        k += 2
    for cipher_num in cipher_nums:
        number += cipher_num*10**k
        k -= 2
    return number


def get_plain_text(plain_nums: list[int], style: str):
    plain_text = ""
    for number in plain_nums:
        if style == "fi":
            plain_text += finnish[number]
        elif style == "en":
            plain_text += english[number]
    return plain_text


def prime_factors(n: int):
    """Split n into primes
    args: 
    n: integer to be split"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    if len(factors) > 2:
        raise Exception(f"Yeah I don't think so. Primes: {factors}")
    return factors


def encrypt_rsa(string: str, style: str, e: int, n: int):
    """
    Steps for RSA encryption
    1. if p and q, n = p*q, fii_n = (p-1)*(q-1)
    2. count decrypt exponent d = invmod(e, fii_n)
    3. for every plainletter m, get ciphernum c as count_down(m**e, n)
    (4. add up every cipher number together into a large num)
    Args:
        string: plaintext to be encryptred
        style: fi or en
        e: exponent number
        n: reducer num"""
    plain=get_plain_nums(string, style)
    cipher = get_cipher_nums(plain, e, n)
    num = turn_nums_into_num(cipher)
    print(cipher, num)


def decrypt_rsa(de_nums: list[int], style: str, n: int, e: int):
    """Steps for RSA decryption.
    1. Get primes from n
    2. Use those to fii_n
    3. Get d by inverse number fii_n and e
    Args:
        de_nums: list of cipher numbers
        style: fi or en
        n: reducer num
        e: exponent num"""
    primes = prime_factors(n)
    fii_n = (primes[0]-1) * (primes[1]-1)
    d = invmod(e, fii_n)
    cipher = get_cipher_nums(de_nums, d, n)
    plain = get_plain_text(cipher, style)
    print(f"Plaintext: {plain}, d: {d}")


def sign_nums(sign_num: int, msg_nums: list[int], n: int):
    """Sign the message numbers.
    Args:
        sign_num: integer which is used to sign
        msg_nums: list of numbers to sign
        n: reducer integer"""
    for i, num in enumerate(msg_nums):
        msg_nums[i] = get_between(num**sign_num, n)
    return msg_nums


def rsa_encryption_with_sign(string: str, style: str, e_a: int, n_a: int, e_b: int, n_b: int, sign_num: int):
    """Steps:
    Args:
        string: string to be encrypted
        style: en or fi
        e_a: exponent num from the sender
        n_a: reducer num from the sender
        e_b: exponent num from the receiver
        n_b: reducer num from the receiver
        sign_num: secret key number"""
    primes = prime_factors(n_a)
    fii_n = (primes[0]-1) * (primes[1]-1)
    d_a = invmod(e_a, fii_n)
    plains = get_plain_nums(string, style)
    ciphers = get_cipher_nums(plains, e_b, n_b)
    sign_num = get_between(plains[0]**sign_num, n_a)
    enc_sign = get_cipher_nums([sign_num], e_b, n_b)[0]
    print(f"c: {ciphers}, r: {enc_sign}")


def rsa_decryption_with_sign(msg_nums: list[int], style: str, e_a: int, n_a: int, e_b: int, n_b: int, sender_sign_num: int):
    """Args:
        string: string to be encrypted
        style: en or fi
        e_a: exponent num from the sender
        n_a: reducer num from the sender
        e_b: exponent num from the receiver
        n_b: reducer num from the receiver
        sender_sign_key: senders sign key"""
    primes = prime_factors(n_b)
    fii_n = (primes[0]-1) * (primes[1]-1)
    d_b = invmod(e_b, fii_n)
    decrypt_msg_num = get_cipher_nums(msg_nums, d_b, n_b)
    decrypt_sender_sing = get_cipher_nums([sender_sign_num], d_b, n_b)[0]
    confirm_sign = get_cipher_nums([decrypt_sender_sing], e_a, n_a)
    plain_text = get_plain_text(decrypt_msg_num, style)
    print(f"MSG: {decrypt_msg_num}, sender sign: {confirm_sign}")


