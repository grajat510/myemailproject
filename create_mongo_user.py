import os
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB without authentication in URI
client = MongoClient(os.getenv('MONGO_URI'))
db = client.admin

try:
    db.command("createUser", os.getenv('MONGO_DB_USERNAME'),
               pwd=os.getenv('MONGO_DB_PASSWORD'),
               roles=["readWrite", "dbAdmin"])
    print("User created successfully.")
except OperationFailure as e:
    if "already exists" in str(e):
        print(f"User '{os.getenv('MONGO_DB_USERNAME')}' already exists.")
    else:
        print(f"Error creating user: {e}")
