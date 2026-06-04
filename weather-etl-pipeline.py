import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

# Load the .env file
load_dotenv()

# Get API key from .env file
API_KEY = os.getenv("API_KEY")

CITY = "thoothukudi"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# EXTRACT
def extract():
    print("Extracting weather data...")
    response = requests.get(URL)
    data = response.json()
    print("Data extracted successfully!")
    return data

# TRANSFORM
def transform(raw_data):
    print("Transforming data...")
    
    transformed = {
        "city": raw_data["name"],
        "country": raw_data["sys"]["country"],
        "temperature": raw_data["main"]["temp"],
        "feels_like": raw_data["main"]["feels_like"],
        "humidity": raw_data["main"]["humidity"],
        "weather": raw_data["weather"][0]["description"],
        "wind_speed": raw_data["wind"]["speed"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    df = pd.DataFrame([transformed])
    print("Data transformed successfully!")
    return df

# LOAD
def load(df):
    print("Loading data into database...")
    engine = create_engine("sqlite:///weather_data.db")
    df.to_sql("weather", con=engine, if_exists="append", index=False)
    print("Data loaded successfully!")
    print("✅ ETL Pipeline Complete!")

# Run all three
raw_data = extract()
clean_data = transform(raw_data)
load(clean_data)