import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connected to database successfully!")
    conn.close()
except Exception as e:
    print(f"Error connecting to database: {e}")
    