Another week, another "I wish I had time for tasks". Let's get to it.

## Task 1

Recycled the random message generator from last week for this task. Cryptodome was so smart that the tag length for GCM/CCM cannot be under 4 bytes, and after running the code for an hour with no match for 4 byte, I switched to partial matches. Getting the code up and running didn't take that long, but the task description didn't specify whether or not to use the same nonce for decryption. At first I did.

The first message will always be the same "this is the first message" and the key used was "this is a16B key". Tags are compared as bytes, but turned into readable text using base64 encoding for readability.

### Using the same nonce for encryptions

### GCM-mode

#### 1-byte partial search

1-byte search doesn't take long, as expected. I ran five searches and the times and matches were the following:
```
Old tag: 6RuirQ==  New msg: ;  New tag: 6U8HbA==
Time 0.0025802000000000047

Old tag: WGAOGw==  New msg: #6  New tag: WG5+ng==
Time 0.034102300000000696

Old tag: znCBSQ==  New msg: P'  New tag: zkvpUA==
Time 0.03516779999999997

Old tag: xD4K7g==  New msg: yd  New tag: xOiOdw==
Time 0.011881799999997611

Old tag: 32O7bA==  New msg: /T7  New tag: 3yT5EQ==
Time 0.04239499999999907
```

#### 2-byte partial search

2-byte partial search has large differences between matches. Matches:
```
Old tag: eeWHeQ==  New msg: $ki  New tag: eeV/eQ==
Time 5.6633766

Old tag: DjN0uA==  New msg: mAU  New tag: DjMTCA==
Time 1.84868569999999

Old tag: qqyJdg==  New msg: tND  New tag: qqxGUA==
Time 0.4587081999999896

Old tag: ltG2DA==  New msg: JgX  New tag: ltGTpw==
Time 0.3839973999999984

Old tag: 1SVCrA==  New msg: zTBE  New tag: 1SWLdw==
Time 7.1573709

Old tag: yFh0Vg==  New msg: b,M  New tag: yFhbnA==
Time 1.7172602000000001
```

#### 3-byte partial search

If 2-byte partial search had large differences between matches, then 3-byte has HUGE differences. During testing I managed to get one match:

```
Old tag: fCGZ6w==  New msg: DVT  New tag: fCGZwA==
Time 10.4968234
```

But other matches took hours to find. Thus I decided to not to search for three bytes.

### CCM-mode

#### 1-byte partial search

1-byte is fast, as expected. Matches:
```
Old tag: v9JciQ==  New msg: 'c  New tag: v2ZHyg==
Time 0.009001493453979492

Old tag: Mq2uLQ==  New msg: dE  New tag: MtEH/w==
Time 0.01000213623046875

Old tag: IMfB7A==  New msg: zx  New tag: IMwWNg==
Time 0.018004655838012695

Old tag: 70hZ+w==  New msg: |G  New tag: 79MvuQ==
Time 0.005001068115234375

Old tag: nqRYIA==  New msg: b"  New tag: niabjQ==
Time 0.003000020980834961
```

#### 2-byte partial search

2-byte search was much faster than in GCM mode. Matches:
```
Old tag: fchwAA==  New msg: v.v  New tag: fcg9Gg==
Time 1.5963592529296875

Old tag: DdoyYw==  New msg: \>#  New tag: Ddo5BQ==
Time 0.43109679222106934

Old tag: +ZCiVA==  New msg: v+v  New tag: +ZDxPA==
Time 5.684293746948242

Old tag: /nbNtA==  New msg: fOO  New tag: /nYIYg==
Time 2.0004518032073975

Old tag: 2vynzQ==  New msg: wFa  New tag: 2vz7hQ==
Time 1.2968573570251465
```

### Random nonces
Since the task itself didn't say anything about nonce usage, I also checked how the partial matches would work with random nonces.

### GCM-mode

#### 1-byte
Matches:
```
Old tag: ti6fSg==  New msg: 7V  New tag: tiNp+A==
Time 0.03000640869140625

Old tag: p047FQ==  New msg: q3  New tag: p4DShw==
Time 0.017003297805786133

Old tag: ouSz/Q==  New msg: gc  New tag: ok3FNw==
Time 0.0019998550415039062

Old tag: vVeHQw==  New msg: Y♀  New tag: vcQKcg==
Time 0.0200042724609375

Old tag: l5qrSg==  New msg: 9$  New tag: l17tmQ==
Time 0.0019989013671875
```

#### 2-byte
Matches:
```
Old tag: QKUIZw==  New msg: j_m  New tag: QKX3hQ==
Time 6.113696813583374

Old tag: d/dkHA==  New msg: y]Z  New tag: d/fZ7g==
Time 3.0446863174438477

Old tag: 4MXN6Q==  New msg: <I6  New tag: 4MUxCg==
Time 8.806028127670288

Old tag: 1NpjMA==  New msg: xU♀  New tag: 1NrrqA==
Time 2.1126866340637207

Old tag: kPxv5g==  New msg: '♂Sr  New tag: kPyxGg==
Time 4.269790410995483
```

### CCM-mode

#### 1-byte
Matches:
```
Old tag: fStbuQ==  New msg: X6  New tag: fbHhbA==
Time 0.03900909423828125

Old tag: FOPz/g==  New msg: 5+$  New tag: FEk+mQ==
Time 0.0050013065338134766

Old tag: pOCUJQ==  New msg: pi  New tag: pCSN3w==
Time 0.010002374649047852

Old tag: ifx1/Q==  New msg: Z.  New tag: iYoWPQ==
Time 0.020004987716674805

Old tag: HRc04g==  New msg: >♀  New tag: HdikZw==
Time 0.005002021789550781
```

#### 2-byte
Matches:
```
Old tag: ZdQi0A==  New msg: tw♂  New tag: ZdQAAg==
Time 0.7831761837005615

Old tag: ReqEUg==  New msg: f]!c  New tag: RepEDw==
Time 2.023667573928833

Old tag: 9g+Shg==  New msg: wQ;  New tag: 9g/hbA==
Time 2.690152406692505

Old tag: uejyyw==  New msg: Tt[  New tag: ueg5Qw==
Time 13.28607964515686

Old tag: VhNRgw==  New msg: OIn  New tag: VhMsqQ==
Time 3.11071515083313
```

### Comparing runtimes

Next I wanted to figure out the average time it took to find the bytes. Running the code for five times and taking their average was not good enough so I ran the code 20 times and compared their times. Running the code for hundred times would have given even better results, but these had to do with the time I had. The results were as followed.

```
Fixed Nonce
1-Byte
CCM: 0.008401894569396972
GCM: 0.013603901863098145

2-Bytes
CCM: 3.1076968908309937
GCM: 3.571850311756134

Random Nonce
1-Byte
CCM: 0.008611464500427246
GCM: 0.010756421089172363

2-Bytes
CCM: 2.3952025413513183
GCM: 3.1883319497108458
```

Here is the comparison in chart form.

![](src/comparisons.png?raw=true "Comparison between runtimes")

As we can see finding partial matches for GCM was bit harder than for CCM. I did some research and the general consensus seems to be that GCM is the better of the two, and the runtimes do support this fact. GCM is not only the more secure option, it is also more efficient of the two.