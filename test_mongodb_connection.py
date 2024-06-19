# test_mongodb_connection.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

try:
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client.get_database(os.getenv('MONGO_DB_NAME'))
    print("Connected to MongoDB successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
