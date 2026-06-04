from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///weather_data.db")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM weather"))
    print("📊 Data in Database:")
    for row in result:
        print(row)