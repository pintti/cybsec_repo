def get_makers(group_num: int):
    makers = []
    num = group_num - 1
    half = num/2
    half = round(half)
    for i in range(2, half):
        nu_num = num / i
        if nu_num % 1 == 0:
            if i not in makers:
                makers.append(i)
                makers.append(int(nu_num))
    return makers


def raise_to_pow(num: int, makers: list[int], divider: int):
    pows = []
    for maker in makers:
        pows.append((maker, pow(num, maker, divider)))
    return pows


def get_public_key(user: int, powed: int, mod: int):
    return pow(powed, user, mod)


def get_together_key(a: int, b: int, mod: int):
    return pow(a, b, mod)
