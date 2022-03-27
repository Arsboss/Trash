import requests

url = input()

while True:
    result = requests.get(url)
    print(result)
