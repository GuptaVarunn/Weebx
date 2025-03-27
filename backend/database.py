import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve MongoDB connection string from environment variable
MONGO_URI = os.getenv("MONGO_URI")

# Basic connection without SSL
try:
    # Create MongoDB client with basic connection
    client = MongoClient(MONGO_URI, connect=True)
    
    # Verify connection
    client.admin.command('ping')
    
    # Select database and collection
    db = client["Blog"]
    collection = db["posts"]
    
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"MongoDB Connection Error: {e}")