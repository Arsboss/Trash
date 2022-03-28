import requests

url = input()

while True:
    result = requests.get('http://' + url)
    print(result)
