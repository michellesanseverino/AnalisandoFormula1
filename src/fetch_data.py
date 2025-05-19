import requests
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["f1_insights"]
collection = db["races"]

def fetch_race_data(season: str, round_number: str):
    url = f"https://ergast.com/api/f1/{season}/{round_number}/results.json"
    response = requests.get(url)
    data = response.json()

    race_info = data['MRData']['RaceTable']['Races']
    if not race_info:
        print(f"Nenhuma corrida encontrada para {season} rodada {round_number}")
        return None

    race = race_info[0]
    race_data = {
        "season": season,
        "round": round_number,
        "race_name": race["raceName"],
        "circuit": race["Circuit"]["circuitName"],
        "date": race["date"],
        "results": []
    }

    for result in race["Results"]:
        race_data["results"].append({
            "position": result["position"],
            "driver": f"{result['Driver']['givenName']} {result['Driver']['familyName']}",
            "constructor": result["Constructor"]["name"],
            "time": result.get("Time", {}).get("time"),
            "status": result["status"]
        })

    return race_data

def save_race_to_db(race_data):
    if not race_data:
        return
    existing = collection.find_one({
        "season": race_data["season"],
        "round": race_data["round"]
    })
    if existing:
        print("Corrida já registrada no banco.")
    else:
        collection.insert_one(race_data)
        print("Corrida salva com sucesso.")
