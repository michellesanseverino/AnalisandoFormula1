import os
import json
import csv

def save_as_json(race_data, folder="data"):
    """
    Salva os dados da corrida como arquivo JSON.
    """
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/race_{race_data['season']}_round_{race_data['round']}.json"
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(race_data, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Dados salvos como JSON em: {filename}")


def save_results_as_csv(race_data, folder="data"):
    """
    Salva os resultados da corrida (lista de pilotos) como arquivo CSV.
    """
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/race_{race_data['season']}_round_{race_data['round']}_results.csv"
    
    fieldnames = ["position", "driver", "constructor", "time"]
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(race_data["results"])
    
    print(f"✅ Resultados salvos como CSV em: {filename}")
