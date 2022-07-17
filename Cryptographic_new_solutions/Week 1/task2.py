from string import ascii_uppercase, ascii_lowercase
from typing import List
from collections import Counter


encrypted_text = "TRLSHAXRNSVKIENUFMEGRVDANEELHOFNSLUGIEFZVATAAGCIYAGIFADWUDHFYIFPOWVSPUMBKOTUOBYYNQWZYEEHBFCYCRZUKIPDZFFOYDBPZTPRBRVRFRBFYESLSXUAALBFIIAVWORLYBAAIAYGWYVNFLCZKHRVBANDRQFQMEYDHUFNFPCFZVNWSMIENVGQJSZHBFFFGKSBFLVWWORLNQRYFRNODAJIGLCZZNTRTOIYCWCSIACKMFYELOSMUOAHHARSXLTALRVQONZLVWMFFESISOKIIHZKRDQUSEJMNVGELRIHWXCAAFSOFNFWWFLTRVORRIYXFQFFBXFRZEYGWNVLVHJQKHNWWFUORVWORLYICDRCBPAGEIGBKUUERITAITGRRQMEYRDYFRRHTRVCGLJQDENQGFFRRVWEKMNVGELRIHWXCAAFSUGLRDRRFRNUSUEVRQHUFNBICGIDVVQUGLVQODPCHOHGIEGROFKEAGBAKOAOMFFPHCNXVSNQRYRTUEIFRLFRHAKHRVCOZEGDZUDPYLQMKIBQGAWOHUKAIK"

def slice_text(n: int, text: str):
    """Used to slice the text into neat little parts."""
    m = 0
    sliced_text = []
    while text:
        slice = text[m:n]
        text = text.removeprefix(slice)
        sliced_text.append(slice)
    return sliced_text

def find_repeats(word_list: List):
    """Finds the repeating words we can use to crack the cipher.
    Words found:
    IEN HBF VWO RLY LCZ KHR MEY FNF QRY FRN VGE LRI HWX CAA WWF FRR
    WORL
    LRIHWX
    RIHWXCA"""
    while word_list:
        word = word_list.pop(0)
        if word in word_list:
            print(word)

def find_most_used_letter(text: str):
    """Used for frequency analysis
    Most used letters are R: 47, F: 45, A: 31, I: 29, V: 27"""
    print(Counter(text).most_common(5))

def get_words():
    test_word_list = open("words.txt", "r").readlines()
    for word in test_word_list:
        word = word.strip()
        if len(word) >= 3 and len(word) < 7:
            decrypt_list(word)

def letter_to_num(letter: str):
    return ascii_uppercase.index(letter)

def num_to_letter(num):
    return ascii_uppercase[num]

def sum_letter_nums(num_list1, num_list2):
    new_nums = []
    for i in range(len(num_list1)):
        num = num_list1[i] - num_list2[i]
        if num < 0:
            num += 26
        new_nums.append(num)
    return new_nums

def decrypt_list(word: str):
    word_numbers = []
    for letter in word:
        word_numbers.append(ascii_lowercase.index(letter))
    sliced_text = slice_text(len(word), encrypted_text)
    fixed_text = []
    for slice_word in sliced_text:
        num_text = [letter_to_num(slice_word[i]) for i in range(len(slice_word))]
        num_text = sum_letter_nums(num_text, word_numbers)
        fixed_text.append([num_to_letter(num_text[i]) for i in range(len(num_text))])
    lists_to_text(fixed_text, word)

def lists_to_text(text_list: list, word: str):
    string = ""
    for text_word in text_list:
        for letter in text_word:
            string += letter
        string += ""
    if "THE" in string:
        print(string)
        print(word, end='\n\n')

#get_words()
print(len(encrypted_text) / 6)
