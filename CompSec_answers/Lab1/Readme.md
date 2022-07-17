# Lab 1: Fuzzing

## Task 1
### 1.1

```
echo "Fuzztest 1337" | radamsa -n 10

Fuzzt 0317

F$PATH'xcalc\x00;xcalc\raaaa%naaaa%d%n$(xcalc)%nNaN!!$+%d\x00\r%p!!!!&#000;Fuzztest 1337$1NaN$

(xa)Fuzztest 1337$1NaN$(xa)Fuzztest 1337

Fuzztest 1337

Fuzztest!290

Fuzztest 170141183460469231731687303715884105727

Fuzztest 340282366920938463463374607431768211456

Fuzztest 4294967297

Fuzzte$+$
+\r\n\u0000\r\0`xcalc`!xcalc\x9223372036854775809a\r%saaaa%d%n!xcalc'xcalcst�170141183460469231731687303715884105729

Fuzztest�91856
```

### 1.2
content of fuzz41.txt

>1 EF

content of fuzz 76.txt

>1 E��1 E����������������������F

command

> kali@kali:~/samples$ for i in `seq 1 100`; do radamsa sample.txt > fuzz$i.txt; done  

&nbsp;

---  


## Task 2

### A)

Compile
> clang -fsanitize=address -O1 -fno-omit-frame-pointer sample.c -o test

Screenshot of the error

![Screenshot of error](ss1.png)

The error is a memory leak, caused by the program not freeing the allocated memory.

### B)



