# dashboard_flask.py

from flask import Flask, render_template
import json
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Carrega JSON
    try:
        with open(os.path.join("data", "data\\last_race.json"), encoding="utf-8") as f:
            race_data = json.load(f)
    except:
        race_data = None

    # Carrega CSV
    try:
        df = pd.read_csv(os.path.join("data", "results.csv"))
    except:
        df = None

    return render_template("templates\\dashboard.html", race_data=race_data, df=df)

if __name__ == '__main__':
    app.run(debug=True)
