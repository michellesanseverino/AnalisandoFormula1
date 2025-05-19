from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_mongo_client():
    return MongoClient(os.getenv("MONGODB_URI"))

def get_race_data():
    client = get_mongo_client()
    db = client["f1"]
    collection = db["races"]
    
    # Busca a última corrida
    last_race = collection.find_one(sort=[("date", -1)])
    
    # Converte os resultados para lista (Chart.js pode usar isso)
    results = list(collection.find().sort("date", -1).limit(5))  # últimos 5
    return last_race, results
