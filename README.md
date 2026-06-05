# 🌤️ Weather ETL Pipeline

A real-time Weather ETL (Extract, Transform, Load) pipeline built with Python and Flask, deployed as a live web application with a split frontend/backend architecture.

## 🔗 Live Demo
👉 **Frontend (Netlify):** [https://fabulous-capybara-a3324e.netlify.app](https://fabulous-capybara-a3324e.netlify.app)

👉 **Backend API (Render):** [https://weather-etl-pipeline.onrender.com](https://weather-etl-pipeline.onrender.com)

## 📌 What it does
- **Extract** — Fetches live weather data from OpenWeather API for any city in the world
- **Transform** — Cleans and structures the raw data into a usable format using Pandas
- **Load** — Stores the cleaned data into a SQLite database automatically
- **Web App** — Displays live weather and full search history on a clean dashboard

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
    ├── app.py                    # Flask REST API (backend)
    ├── weather-etl-pipeline.py   # Core ETL pipeline script
    ├── verify.py                 # Database verification script
    ├── requirements.txt          # Python dependencies
    ├── Procfile                  # Render deployment config
    ├── .gitignore                # Ignores .env file
    └── templates/
        └── index.html            # Frontend UI (deployed on Netlify)

## ⚙️ How to run locally

1. Clone the repo

        git clone https://github.com/jonathlazar/weather-etl-pipeline.git

2. Install dependencies

        pip install -r requirements.txt

3. Create a `.env` file and add your API key

        API_KEY=your_openweather_api_key

4. Run the app

        python app.py

5. Open `http://127.0.0.1:5000`

## 🔑 Get your free API key
Sign up at [openweathermap.org](https://openweathermap.org) — it's completely free!

## 👨‍💻 Author
**Jonath Lazar G**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/jonath-lazar-data)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/jonathlazar)