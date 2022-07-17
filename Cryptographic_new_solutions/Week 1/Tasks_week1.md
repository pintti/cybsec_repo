# Week 1

## Task 1.

For this task the general idea was quite simple. Since both the message and the produced cipher text are known, with a simple XOR operation it is possible to figure out the keys used in the one-time pad. 

### Task 1.2
No, it is not possible to produce longer than 8 character ciphertexts when the message is 8 characters long. If the message were longer, then so would the ciphertext, but that would require you to reuse the one time pad, which makes it more unsecure than having the pad and the message be both the same length.

### Task 1.3
The binary for the one time pad is 

Binary | Hex
--|--
0b00100001 | 0x21
0b01111100 | 0x7c  
0b01111111 | 0x7f 
0b00000101 | 0x5 
0b01001001 | 0x49 
0b01110001 | 0x71 
0b11000000 | 0xc0 
0b00001110 | 0xe

One time pads are malleable when the attacker is in possession of one ciphertext. If an attacker were to intercept ciphertext C1, they could generate another ciphertext C2 that would still be valid for the receiver as C1 ⊕ C2 = 1. 


## Task 2.

To tell you the truth, I was pretty lost after figuring out the approximate size of the key. Using my code, I figured out that the key was most likely a six letter word, or little less likely, a four letter word. I used Kasiski examination to figure out the approximate. Since the four letter sequence was pretty different from the found six letter and seven letter sequences, I thought that it was more likely that the key word would be six lettered, rather than four. 

But then I got stuck here. I tried using frequency analysis, but I was not able to make heads or tails what I should have done with that information after that. The column thing sounded like it could work, so perhaps I'll try it bit later on.

Anyways, to get through this task, I then decided to use a little bit bruteforce. I got a random list of 10 000 words from some education site, inserted it into the code, and to cover all my bases I allowed the brute forcer to use word with three to six letters. Then by checking which of the strings the brute forcer made had the word "THE" in them, I was able to find the text and the key word.

Not very sophisticated, but hey, it worked.

### Task 2.1
The secret key is RANDOM. Little over 92 permutations were used.

### Task 2.2
The text is from "The Moral Character of Cryptographic Work" by Phillip Rogaway.