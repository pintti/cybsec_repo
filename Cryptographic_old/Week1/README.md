## Task 1

Using task1.py we can solve the pad used for the original ciphertext.

### Task 1.1

Using the original pad on 'No Rauli', we get a ciphertext 'o‼_W(♦¬g'.

### Task 1.2

I chose to cipher plaintext 'Vitonen!' Using the pad we have, we got a ciphertext of 'w§♂j'¶®/'. It is not possible to produce longer ciphertexts than 8 letters because our pad is only 8 letters long. 

### Task 1.3

This is the one-time pad in binary format.

00100001
01111100
01111111
00000101
01001001
01110001
11000000
00001110

One-time pad is malleable, due to the way it's built. If an attacker has the ciphertext, he can figure out another ciphertext of C_2 = C_1 XOR 1, with the same pad.

## Task 2

This task was pretty daunting to be fair. I first started approaching it by using Kasiski examination, and from that I could estimate the keyword being 6 letters long due to finding a 6-letter long duplet and longer duplets were the six one but with some padding. 

Next step I found a comprehensive list of 6-letter words in english on web, raked that list and ran that word through the list, trying to find a proper word that 6-letter nonsense would turn into. No luck, even if words unfelt and reddle did fit.

So what I had to do was to go through the text with every single word I had raked. That's 15 thousand words. Reading every single answer manually would have taken so much time that I had to come up with something. Due to the way task 2.2 was worded, I could guess that the text had something to do with cryptography, so I made it so that if the word "crypto" would appear in the text, it'd stop churning through the words. And finally, I found the answer.

### Task 2.1

The secret key is "random". I don't quite understand what permutations mean in this context, if it means how many times the word was used to change the text, the answer would be 93.

### Task 2.2

The text is from "The Moral Character of Cryptographic Work" by Phillip Rogaway. 

## Task 3

### Task 3.1

As of right now, the differences between `/dev/urandom` and `/dev/random` are rather minimal. `/dev/urandom` gets the numbers from CSPRNG directly, while `/dev/random` uses it to generate entropy pools it uses to generate random numbers. Perhaps the biggest difference between the two is that `/dev/random` starts blocking if the entropy count goes too low. This slows programs and makes the user wait around for more entropy to generate.

Before `/dev/random` was suggested as the more secure option, due to the way it blocks if entropy pools are empty, but nowadays it's an agreed fact that `/dev/random` is old and deprecated interface and `/dev/urandom` should be used instead (https://man7.org/linux/man-pages/man4/random.4.html). There are even talk about removing the blocking pool of `/dev/random` which would bring it even closer to `/dev/urandom` (https://lwn.net/Articles/808575/).

### Task 3.2

All results can be found in src as textfiles.

For a manual method, I chose to roll four different dice (D6, D10, D12 and D20) and use their sum as a random number. The range would be between 4 to 48. 

As for Python its a simple random.randint in between 0 and 1000.

