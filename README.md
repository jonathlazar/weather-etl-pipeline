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