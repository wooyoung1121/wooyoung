import requests

def get(path):
    return requests.get(path)


print(get('http://localhost:8080/wooyoung'))