from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))
db = client["f1_database"]

@app.route("/")
def dashboard():
    last_race = db["races"].find_one(sort=[("date", -1)])
    next_race = db["next_race"].find_one()
    top_pilots = list(db["standings_drivers"].find().sort("points", -1).limit(5))
    top_teams = list(db["standings_constructors"].find().sort("points", -1).limit(5))

    return render_template("dashboard.html", last_race=last_race, next_race=next_race, top_pilots=top_pilots, top_teams=top_teams)

if __name__ == "__main__":
    app.run(debug=True)