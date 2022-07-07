## Task 1

### Task 1.1

genrsa - 2048 bit - time taken: 0,060s  
genrsa - 8 bit - time taken: 0,003s  
genrsa - 4096 bit - time taken: 1,164s  
genrsa - 10240 bit - time taken: 28,583s  

dsparam - 2048 bit - time taken: 0,333s  
gendsa - 2048 bit - time taken: 0,003s  
dsparam - 8 bit - time taken: 0,024s  
gendsa - 8 bit - time taken: 0,002s  
dsparam - 4096 bit - time taken: 1,850s  
gendsa - 4096 bit - time taken: 0,004s  
dsparam - 10240 bit - time taken: 59,709s  
gendsa - 10240 bit - time taken: 0,010s  

genpkey - 2048 bit - time taken: 0,037s  
genpkey - 8 bit - time taken: not allowed  
genpkey - 4096 bit - time taken: 0,375s  
genpkey - 10240 bit - time taken 3,523s  

dsparam is very slow compared to the other two. genrsa is almost comparable to genpkey with smaller bit lengths, but as bit length starts to go over the 2048 bit mark it also slows down heavily.

### Task 1.2

Legacy commands use PKCS1 and PKCS8, while newer commands use PKCS12. genpkey uses PKCS8.

### Task 1.3

cat or less commands.

## Task 2

CRC file can be found in the src folder.


