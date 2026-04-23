def load_data(df):
    df.to_csv("data/weather_data.csv", index=False)
    print("Data saved successfully!")