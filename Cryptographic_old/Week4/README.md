## Task 1

Code can be found in src/Task1.py

### Task 1.1

Using ChaCha20, I got the following keystream:
```
[12, 132, 165, 150, 125, 45, 232, 34, 25, 190, 124, 218, 19, 32, 129, 132, 103, 129, 142, 91, 214, 75, 158, 236, 175, 15, 167, 173, 38, 53, 195, 62, 46, 217, 197, 37, 20, 126, 35, 93, 64, 36, 210, 177, 40, 105, 76, 98, 200]
```
When we checkout the ciphertext in number form we get:
```
[65, 235, 211, 243, 93, 89, 128, 71, 57, 202, 29, 184, 127, 69, 242, 164, 19, 238, 174, 47, 190, 46, 190, 156, 206, 123, 206, 194, 6, 84, 176, 30, 93, 182, 170, 75, 52, 31, 80, 125, 48, 75, 161, 194, 65, 11, 32, 7, 233]
```
Using the the keystream and XORing it with the new plaintext, we get the following ciphertext:
```
[65, 235, 211, 243, 93, 89, 128, 71, 57, 221, 20, 187, 122, 82, 242, 164, 19, 238, 174, 47, 190, 46, 190, 132, 192, 122, 212, 200, 6, 84, 176, 30, 93, 182, 170, 75, 52, 31, 80, 125, 48, 75, 161, 194, 65, 11, 32, 7, 233]
```
Decrypting the new ciphertext using ChaCha20 decrypt we get the chair plaintext. 

The ciphertexts are almost the same, but with five different numbers due to the difference between words 'table' and 'chair'. When looked at in plaintext format the ciphertexts look the following:
```
Cipher1: AëÓó]YG9Ê↔¸⌂Eò¤‼î®/¾.¾Î{ÎÂ♠T°▲]¶ªK4▼P}0K¡ÂA♂ é
Cipher2: AëÓó]YG9Ý¶»zRò¤‼î®/¾.¾Î{ÎÂ♠T°▲]¶ªK4▼P}0K¡ÂA♂ é
```

Usually the keystream changes after using it once, either due to using a new nonce or key or due to the algorithm implemented in code. If we manage to get the earlier used keystream, it's possible to modify and read the earlier texts.

### Task 1.2

Using the phrases 'Man, I could really go for a beer right now.' and 'Men, I could really go for a beer right now.' and encrypting them with almost identical keys I got the following ciphertexts:

```
Cipher1: AåËº]dÈAvË►¾3Räå♂í÷{±$¾À}Ì♠W¦[\ù·Ls▬W}.K¥
Cipher2: 02~sÜ=»♦ãÖº¤¶;süü`G\Ä=©B→ÂfY↨\4¹ÿ¢ööCN­Y
```

I could not find any patterns in the ciphers in text or number format nor can I see any relations between the plaintexts that could be seen out of the ciphertexts.

### Task 1.3

I ran all the encryptions using the same key and with a random nonce for the ChaCha20. Differences were the following:
```
AES-CBC 0.0009318999999999994
AES-CTR 0.0001900000000000096
ChaCha20 0.00014540000000000386
```
As we can see, AES-CTR and ChaCha20 are faster than CBC. I believe it's mostly due to CBC needing extra padding. ChaCha20 is the most efficient, but the difference between it and CTR are not that great. Relatively the differences are very small due to the time it takes to run being only microseconds, but when used with larger data the difference could be much greater.

## Task 2

To form the messages I created a function which cycles through the alhabet starting from a and adding more letter whenever all the letters in the message were z. (src/task2.py)

### Task 2.1

#### Using MD5:
For the first two bytes finding the collision took 0.027 seconds and the collision was:
```
Message: nr Hash: 0ab3e5d0801aea3f3758bcbd812e8f10
Message: fm Hash: 0ab34ca97d9946591bf89817789cb5de
```
For three bytes the first collision took 6.5 seconds to find and the collision was:
```
Message: hgv Hash: 814b9c2ee0ac2ee0612dd11ca3840240
Message: adu Hash: 814b9c1a48f94893e1f2ca9f7b83c17f
```
For four bytes the first collision took 616 seconds to find and the collision was:
```
Message: bwma Hash: a986d9ee140c5acbf0d51c00bc5a7810
Message: kot Hash: a986d9ee785f7b5fdd68bb5b86ee70e0
```

#### Using SHA-1
For the first two bytes finding the collision took 0.16 seconds and the collision was:
```
Message: zc Hash: 029a3fcb010f8f92628023b595f00551a85179ef
Message: nj Hash: 029a55633b5f056d2e17ce0ebe0382658a9af06d
```
For three bytes the first collision took 0.2 seconds and the collision was:
```
Message: adb Hash: fa1143dea12bffbbc1aa99d5da2ec811d63b5127"
Message: du Hash: fa114377ef35b25ecaa4d57e5084641543e02588
```
Using the first function I was not able to locate a collision even with million different messages.

#### New random message function!

When I finished the new random message generator for task 2.2, I decided that I needed to redo this task. Mostly because I was annoyed that I was not able to find the four byte SHA-1.

#### Using SHA-1
For the first two bytes finding the collision took 0.015 seconds and the collision was:
```
Message: 0m Hash: 4d2216bc6c8db363c99457bec0bae83bd8bec2ca
Message: c^ Hash: 4d22e70f5e855c2663f020555d2d1cf5c51a9174
```
For three bytes the first collision took 2.3 seconds and the collision was:
```
Message: l♀ Hash: cf2c070eb9795beb987443e9ee0b09283a149356
Message: [- Hash: cf2c07d3518b8d4d26e27049d9fa1202730a7245
```
For four bytes the first collision took 112.7 seconds! Well before this I ran the code for 10 minutes and got no collisions so yeah, random :D Anyways the collision:
```
Message: L~A Hash: 3605a269f56cbdb6bd09ac6bcfcf8389ee1b1e74
Message: K)' Hash: 3605a269f56cbdb6bd09ac6bcfcf8389ee1b1e74
```
#### Using MD5
For the first two bytes finding the collision took 0.013 seconds and the collision was:
```
Message: :) Hash: 50585be4e3159a71c874c590d2ba12ec
Message: . Hash: 5058f1af8388633f609cadb75a75dc9d
```
For three bytes the first collision took 5.2 seconds to find and the collision was:
```
Message: XR Hash: 6e029fb0cac7800630850e5f6a2f5567
Message: PW Hash: 6e029fbfa817dfc458598a5d38a6755f
```
For four bytes the first collision took 1641.5 (Jesus) seconds to find and the collision was:
```
Message: (literally nothing on console) Hash: 394296422aa528d68684f06a58547e86
Message: &.H Hash: 394296428f45fd44baf3e23aac9173c1
```
Interestingly enough I could not manage to find the above hash. It's something I suppose.


### Task 2.2

I used MD5 for the preimage task. At first I ran it with the old message maker, but I could not find any matches even with a million tries. I needed a new message generator, one that generated more complex random messages. So I made one.

Finding the first two zeros took 0.00063 seconds and the message and hash was the following (this was also picked up by the old code)
```
Message: mj Hash: 007de96adfa8b36dc2c8dd268d039129
```
For four leading zeroes it took 0.26 seconds and the message and hash was the following:
```
Message: 8k$ Hash: 00005c11e188ec1d85a943c3a581c47b
```
For six leading zeroes it took 11.0 seconds the message and hash was the following:
```
Message: JkfQ Hash: 0000009cb80a04114d2191fbb3501448
```


### Task 2.3

Let's compare the times it took to run the code.

![Time table](src/time_differences.png?raw=true "Time differences")

Here we can see the times it took to find the different byte collisions. For the first two byte collisions the time taken was rather minimal and no major differences can be seen. Only the SHA-1 old message generator took more time than the others (0.16 seconds when compares to the sub 0.03 seconds).

For three byte collisions we start to see slight differences between the codes. Finding a SHA-1 collision using old message generator took only 0.2 seconds while others took seconds. 

Finally for the four byte collisions we see some huge differences. Fastest was the new SHA-1 code. Old SHA-1 never got a collision. The new MD5 took longest with taking almost half an hour

In my opinion timing the collisions isn't really fair as the time is highly dependant on the messages you run through the code. If the messages line up properly when picked randomly, finding a 4-byte collision might take only 1 second. This is highly improbable of course, but I think it's a valid point. As the second message generator generated random messages when compared to th earlier version, it could give wildly different runtimes. 

Now let's see the memory usage. All the images are the amount of memory it took to find the 4-byte collision.

![MD5 old](src/MD5_4-byte.png?raw=true "MD5 Old generator") 

Old generator MD5.

![](src/MD5_4-byte_random.png?raw=true "MD5 New generator")

New generator MD5

![](src/SHA-1_4-byte.png?raw=true "SHA-1 new generator")

New generator SHA-1

I was surprised by how little memory it took to store hundreds of thousands of hash values, but Python dictionaries are magic. Or just smart use of hashes. Still, we can see that the longer the code ran, more memory was needed. The rise in memory usage isn't huge as is obvious when comparing the new SHA-1 and MD5 memory usages. The new SHA-1 code ran only for around two minutes and took little over 40 MiB in memory. The new MD5 in turn took 1600 seconds, yet the increase in memory usage was only about 10 MiB.

I see no huge differences between the computation or memory requirements of the implementations. If I would have tied running the script to my GPU, running through the hashes and tables would have been much faster. And I don't believe my implementations to be even good, there must be way more efficient ways to do these. 

But there was one thing I was suprised of. See the following picture.

![](src/MD5_zeroes.png?raw=true "MD5 zero memory usage")

This is the amount of memory it took to find the six leading zeros in MD5 hash. My code shouldn't store anything, yet it used almost 500 MiB in memory?! Only explanation I can guess is that the script doesn't actually store the new values over old ones, but rather leaves the old values as leftover data. 

