from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, text
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
engine = create_engine("sqlite:///weather_data.db")

# EXTRACT
def extract(city):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    return response.json()

# TRANSFORM
def transform(raw_data):
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
    return transformed

# LOAD
def load(data):
    df = pd.DataFrame([data])
    df.to_sql("weather", con=engine, if_exists="append", index=False)

# ROUTES
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    raw_data = extract(city)
    if raw_data.get("cod") != 200:
        return jsonify({"error": "City not found!"})
    data = transform(raw_data)
    load(data)
    return jsonify(data)

@app.route("/history")
def history():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM weather ORDER BY timestamp DESC"))
        rows = [dict(row._mapping) for row in result]
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)