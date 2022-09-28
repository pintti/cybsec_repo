from urllib import request
import requests as req
import json
from threading import Thread, local
from queue import Queue

thread_local = local()

def main():
    with open("wordlist.json") as json_file:
        wordlist = json.load(json_file)
    brute(wordlist)


def brute_r(wordlist):
    with req.Session() as session:
        for key in reversed(wordlist):
            print("Word: ", wordlist[key], " key num: ", key)
            r = session.post("http://localhost:5000/ovi/", json={"answer":wordlist[key]})
            if r.status_code != 404:
                print("SUCCESS")
                print("Pass: ", wordlist[key])
                return


def brute(wordlist):
    with req.Session() as session:
        for key in wordlist:
            print("Word: ", wordlist[key], " key num: ", key)
            r = session.post("http://localhost:5000/ovi/", json={"answer":wordlist[key]})
            if r.status_code != 404:
                print("SUCCESS")
                print("Pass: ", wordlist[key])
                return

if __name__=="__main__":
    main()
    #V4apUkk4m3Hu