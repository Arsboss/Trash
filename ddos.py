import requests


while True:
    result = requests.get('http://cogentv2.dstat.org/')
    print(result)
