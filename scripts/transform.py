import pandas as pd

def transform_data(raw_data):
    transformed = {
        "city": raw_data["name"],
        "temperature": round(raw_data["main"]["temp"] -273.15,2),
        "humidity": raw_data["main"]["humidity"],
        "weather": raw_data["weather"][0]["description"]
    }

    df = pd.DataFrame([transformed])
    return df