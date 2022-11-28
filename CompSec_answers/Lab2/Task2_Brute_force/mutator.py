import string
import json

def mutate(word: str):
    new_words = [word]
    wordlist = [word]
    while new_words:
        new_word = new_words.pop(-1)
        split_word = list(new_word)
        for i in range(len(new_word)):
            letter = split_word[i]
            if leet(letter) != letter:
                split_word[i] = leet(letter)
                nu_word = "".join(split_word)
                if nu_word not in wordlist:
                    new_words.append(nu_word)
                    wordlist.append(nu_word)
            letter = letter_change(letter)
            split_word[i] = letter
            nu_word = "".join(split_word)
            if nu_word not in wordlist:
                new_words.append(nu_word)
                wordlist.append(nu_word)
    return wordlist


def letter_change(letter:str):
    if letter in string.ascii_lowercase:
        return string.ascii_uppercase[string.ascii_lowercase.index(letter)]
    if letter in string.ascii_uppercase:
        return string.ascii_lowercase[string.ascii_uppercase.index(letter)]
    return letter


def leet(letter: str):
    if letter == 'a' or letter == "A":
        return '4'
    if letter == 'e' or letter == "E":
        return '3'
    return letter


def dictify(wordlist):
    word_dict = {}
    for i in range(len(wordlist)):
        word_dict[i] = wordlist[i]
    return word_dict


def main():
    word = "vaapukkamehu"
    wordlist = {}
    cycle = 0
    wordlist = mutate(word)
    word_dict = dictify(wordlist)
    file = open("wordlist.json", "w")
    file.write(json.dumps(word_dict, indent=4))


if __name__=="__main__":
    main()
