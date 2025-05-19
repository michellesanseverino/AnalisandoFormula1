# -*- coding: utf-8 -*-

import json
import pandas as pd
import os
import matplotlib.pyplot as plt # type: ignore

def load_json_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def show_last_race_summary(data):
    print(f"\n🏁 Última Corrida: {data['race_name']} ({data['season']})")
    print(f"📍 Local: {data['circuit_name']} - {data['location']['locality']}, {data['location']['country']}")
    print("📆 Data:", data["date"])
    print("\n🏆 Top 3 Pilotos:")
    for i, result in enumerate(data["results"][:3], start=1):
        print(f"{i}º - {result['driver']} ({result['constructor']})")

def plot_results_csv(csv_path):
    df = pd.read_csv(csv_path)
    
    # Número de pilotos por corrida
    piloto_por_corrida = df.groupby('race_name')['driver'].count()
    piloto_por_corrida.plot(kind='bar', figsize=(10,5), title='Número de pilotos por corrida')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    json_path = os.path.join("..", "data", "last_race.json")
    csv_path = os.path.join("..", "data", "results.csv")

    try:
        data = load_json_data(json_path)
        show_last_race_summary(data)
    except FileNotFoundError:
        print("❌ Arquivo JSON da corrida não encontrado.")

    try:
        plot_results_csv(csv_path)
    except FileNotFoundError:
        print("❌ Arquivo CSV com resultados não encontrado.")
