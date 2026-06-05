# 🌤️ Weather ETL Pipeline

I built this project to understand how data engineering works in practice — specifically how raw data gets collected, cleaned, and stored. It pulls live weather data from any city, processes it, and saves it to a database. Everything runs as a live web app.

## 🔗 Live Demo
👉 **Website:** [https://fabulous-capybara-a3324e.netlify.app](https://fabulous-capybara-a3324e.netlify.app)

👉 **Backend API:** [https://weather-etl-pipeline.onrender.com](https://weather-etl-pipeline.onrender.com)

## 📌 What it does
- Hits the OpenWeather API and pulls live weather data for any city you search
- Cleans and organizes that messy raw data into something readable
- Saves every search into a local database with a timestamp
- Shows it all on a clean web interface with a full search history table

## 🛠️ Tech Stack
| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Flask** | Web framework / REST API |
| **Pandas** | Data transformation |
| **SQLAlchemy** | Database connection |
| **SQLite** | Local database storage |
| **Flask-CORS** | Cross-origin resource sharing |
| **OpenWeather API** | Live weather data source |
| **Netlify** | Frontend deployment |
| **Render** | Backend deployment |
| **Git/GitHub** | Version control |

## 🏗️ Architecture

User → Netlify (Frontend) → Render (Flask API) → OpenWeather API → SQLite Database

## 📁 Project Structure

    weather-etl-pipeline/
    ├── app.py                    # Flask REST API
    ├── weather-etl-pipeline.py   # Core ETL script
    ├── verify.py                 # Check what's in the database
    ├── requirements.txt          # Dependencies
    ├── Procfile                  # Render config
    ├── .gitignore                # Keeps .env off GitHub
    └── templates/
        └── index.html            # Frontend

## ⚙️ How to run locally

1. Clone the repo

        git clone https://github.com/jonathlazar/weather-etl-pipeline.git

2. Install dependencies

        pip install -r requirements.txt

3. Create a `.env` file with your API key

        API_KEY=your_openweather_api_key

4. Run it

        python app.py

5. Open `http://127.0.0.1:5000`

## 🔑 API Key
Get a free one at [openweathermap.org](https://openweathermap.org) — takes 2 minutes to sign up.

## 👨‍💻 Author
**Jonath Lazar G**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/jonath-lazar-data)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/jonathlazar)