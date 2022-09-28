import hashlib
import json

import requests

def main():
    with open("wordlist.json") as json_file:
        wordlist = json.load(json_file)
    for key in wordlist:
        secret_token = wordlist[key].encode('utf-8')
        hashed_pass = hashlib.sha1(secret_token).hexdigest()
        if '171108b4c4ca0983911f6af233de18879ae96bbd' == hashed_pass:
            return wordlist[key]
    
key = main()
r = requests.post("http://localhost:5000/ovi/", json={"answer":key})
print(r.text)
print(r.statuscode)