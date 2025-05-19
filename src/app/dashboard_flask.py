from flask import Flask, render_template, jsonify
from db import get_race_data
import json

app = Flask(__name__)

@app.route('/')
def index():
    last_race, recent_races = get_race_data()
    return render_template("dashboard.html", race=last_race, races=recent_races)

# Rota para gráfico dinâmico
@app.route('/chart-data')
def chart_data():
    _, recent_races = get_race_data()

    data = {
        "labels": [r["race_name"] for r in recent_races],
        "points": [sum([int(p["points"]) for p in r["results"]]) for r in recent_races]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
