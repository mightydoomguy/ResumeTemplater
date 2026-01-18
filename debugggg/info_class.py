import requests
from main import token
API_KEY = token
API_URL = "https://api.mistral.ai/v1/models"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(API_URL, headers=headers)
dic = response.json()
for i in dic['data']:
    print(i)
