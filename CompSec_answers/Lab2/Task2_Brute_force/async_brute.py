import requests_async as req

def main():
    with open("wordlist.txt") as file:
        wordlist = file.readlines()
    print(wordlist)
    brute(wordlist)


async def brute(wordlist):
    async with req.Session() as session:
        url = "http://localhost:5000/ovi/"
        for line in wordlist:
            line = line.strip()
            line = line.replace("\\r\n", "")
            print(line)
            r = await req.post(url=url, json={"answer":f"{line}"})
            print(r.status_code)
            if r.status_code != 404:
                print("SUCCESS")
                print("Pass: ", line)
                return

if __name__=="__main__":
    main()
    #V4apUkk4m3Hu