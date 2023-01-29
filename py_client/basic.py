import requests

#endpoint = "https://www.httpbin.com/status/200"
#endpoint = "https://www.httpbin.org/anything"
#endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/api/"

#get = requests.get(endpoint, json={"query": "Hello World"})

get = requests.get(endpoint,params={"abc":123}, json={"query":"Geek World!"})

print(get.text)
print(get.json())
print(get.status_code)
