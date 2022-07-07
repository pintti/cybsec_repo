## Task 1

### Task 1.1

Command used to generate RSA key.
```
# Generate a new private key
openssl genpkey -out key -algorithm RSA 
# Generate a new public key
openssl pkey -in key -pubout -out pkey
```
Didn't specify anything else as that should be enough for this exercise. The key can be found in /src folder.

Next I made a small text file to be encrypted, containing a message and encrypted the file.
```
# Encrypt the message file using public key
openssl rsautl -encrypt -inkey pkey.pem -pubin -in msg.txt -out encrypt.txt
```
Both the msg.txt and ecrypt.txt can be found in /src folder.

### Task 1.2

Next the signing.
```
# Create a hash for the message
openssl dgst -sha256 encrypt.txt > hash
# Use hash with private key to sign the file
openssl rsautl -sign -inkey key.pem -keyform PEM -in hash > signature.txt
```
Hash and signature are in the /src folder.