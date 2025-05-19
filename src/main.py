from save_files import save_as_json, save_results_as_csv
from src.fetch_data import save_race_to_db, fetch_race_data

def main():
    print("==== F1 Insights Automator ====")
    season = input("Digite o ano da temporada (ex: 2023): ")
    round_number = input("Digite o número da rodada (ex: 5): ")

    print("Coletando dados...")
    race_data = fetch_race_data(season, round_number)

    if race_data:
        print(f"Corrida: {race_data['race_name']} em {race_data['date']}")
        print("Salvando no banco de dados...")
        save_race_to_db(race_data)
        save_as_json(race_data)
        save_results_as_csv(race_data)
    else:
        print("Erro ao coletar dados.")

if __name__ == "__main__":
    main()
