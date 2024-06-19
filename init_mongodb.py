import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client.get_database(os.getenv('MONGO_DB_NAME'))

users_collection = db['users']
users_collection.insert_one({
    'email': 'testuser@example.com',
    'password': 'password'
})

print("Initialized MongoDB with initial data.")
