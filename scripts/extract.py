import requests

API_KEY = "2a4ce4b34e4acebeaf1831eba0740341"
CITY = "Dallas"

def extract_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data