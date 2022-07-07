import requests

encrypted_word = list("TRLSHAXRNSVKIENUFMEGRVDANEELHOFNSLUGIEFZVATAAGCIYAGIFADWUDHFYIFPOWVSPUMBKOTUOBYYNQWZYEEHBFCYCRZUKIPDZFFOYDBPZTPRBRVRFRBFYESLSXUAALBFIIAVWORLYBAAIAYGWYVNFLCZKHRVBANDRQFQMEYDHUFNFPCFZVNWSMIENVGQJSZHBFFFGKSBFLVWWORLNQRYFRNODAJIGLCZZNTRTOIYCWCSIACKMFYELOSMUOAHHARSXLTALRVQONZLVWMFFESISOKIIHZKRDQUSEJMNVGELRIHWXCAAFSOFNFWWFLTRVORRIYXFQFFBXFRZEYGWNVLVHJQKHNWWFUORVWORLYICDRCBPAGEIGBKUUERITAITGRRQMEYRDYFRRHTRVCGLJQDENQGFFRRVWEKMNVGELRIHWXCAAFSUGLRDRRFRNUSUEVRQHUFNBICGIDVVQUGLVQODPCHOHGIEGROFKEAGBAKOAOMFFPHCNXVSNQRYRTUEIFRLFRHAKHRVCOZEGDZUDPYLQMKIBQGAWOHUKAIK")
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
test_word = ['t', 'h', 'e']

def turn_word_into_mince(n, word, lista):
    for k in range(0, len(word), n):
        letter_list = []
        for i in range(n):
            try:
                letter = word[i+k].lower()
                letter_list.append(letter)
            except IndexError:
                break
        lista.append(letter_list)
    return lista

def find_same_words(lista1):
    seen = []
    duplicates = []
    for word in lista1:
        if word not in seen:
            seen.append(word)
        else:
            duplicates.append(word)
    return duplicates
            
def letter_freq(word):
    letter_list = {}
    for letter in word:
        if letter not in letter_list:
            letter_list[letter] = 0
        else:
            letter_list[letter] += 1
    return letter_list

def word_to_numbers(word):
    number_list = []
    for letter in word:
        index = english.index(letter)
        number_list.append(index)
    return number_list

def numbers_to_word(cipher_numbers, word_numbers, n):
    word = ''
    for i in range(n):
        index = cipher_numbers[i] - word_numbers[i]
        if index < 0:
            index += 26
        word += english[index]
    return word

# I am leaving this here to show that at first I tried to break this by hand. Got bored fast and decided to automate it.
"""
def try_word_to_dupe(dupes, n):
    dupe_numbers = word_to_numbers(dupes)
    word = input('Input a word to match: ')
    while word:
        word_numbers = word_to_numbers(word)
        key_word = numbers_to_word(dupe_numbers, word_numbers, n)
        print(key_word, 'is your keyphrase. Press enter to end or enter a new word.')
        word = input()
        if word == '':
            break
"""

def try_word_to_dupe(dupes, n):
    dupe_numbers = word_to_numbers(dupes)
    word_list = pull_list("http://www.poslarchive.com/math/scrabble/lists/common-6.html")
    letter = 'a'
    for key_word in word_list:
        text_numbers = word_to_numbers(key_word)
        word = numbers_to_word(dupe_numbers, text_numbers, n)
        """
        if key_word in word_list:
            print(key_word, 'is the key,', word, 'is the word.')
            input()
        """
        print(key_word, 'is the key,', word, 'is the word.')
        use_word_to_decrypt(key_word, encrypted_word, n)

def use_word_to_decrypt(key_word, en_word, n):
    i = 0
    key_numbers = word_to_numbers(key_word)
    new_sentence = ''
    for letter in en_word:
        new_index = (english.index(letter.lower()) - key_numbers[i]) % 26
        new_sentence += english[new_index]
        i += 1
        if i > n-1:
            i = 0
    print(new_sentence)
    if "crypto" in new_sentence:                                # It's a cryptocourse, so believing that the text would have the word 'crypto' in it. 
        input()

def pull_list(link):
    pull = requests.get(link)
    text = pull.text
    text = text.partition('aahing')[2]
    text = text.partition('zombis')[0]
    text = text.split()
    return text




for i in range(3, 7):                                           # I used this range for the Kasiski examination to figure out 6 was the most probable key length.
    lista = turn_word_into_mince(i, encrypted_word, [])
    new_dupes = find_same_words(lista)
print(len(lista))
input()
try_word_to_dupe(new_dupes[0], i)




"""key = random"""