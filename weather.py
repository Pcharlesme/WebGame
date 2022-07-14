from urllib import response
from wsgiref.util import request_uri
import requests

API_KEY = "716e797fc0b2ede32bf5b7d68060c431"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_uri =f"{BASE_URL}?appid= {API_KEY}&q={city}"
response = requests.get(request_uri)

if response.status_code ==200:
    data = response.json()
    print(data)
else: 
    print("Invalid An error Occurred")