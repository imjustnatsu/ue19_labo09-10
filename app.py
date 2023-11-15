import requests

url = "https://api.punapi.com/random"
response = requests.get(url)
data = response.json()

print("Joke : ", data['joke'])
