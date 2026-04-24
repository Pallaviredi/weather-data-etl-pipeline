import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY")

def extract_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        raise Exception(f"API Error: {data.get('message', 'unknown error')}")
    
    print(data)
    return data