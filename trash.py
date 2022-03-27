import requests
from fake_useragent import UserAgent

ua = UserAgent()

url = input()

headers = {'User-Agent': ua.chrome}

while True:
    result = requests.get(url, headers=headers)
    print(result)
