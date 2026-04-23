import pandas as pd

def transform_data(raw_data):
    transformed = {
        "city": raw_data["name"],
        "temperature": raw_data["main"]["temp"],
        "humidity": raw_data["main"]["humidity"],
        "weather": raw_data["weather"][0]["description"]
    }

    df = pd.DataFrame([transformed])
    return df