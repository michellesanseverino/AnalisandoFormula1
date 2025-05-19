# dashboard_app.py

import streamlit as st
import pandas as pd
import json
import os

# Função para carregar JSON
def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Caminhos
json_path = os.path.join("data", "last_race.json")
csv_path = os.path.join("data", "results.csv")

# Título
st.title("🏎️ F1 Insights Dashboard")

# JSON
try:
    race = load_json(json_path)
    st.subheader(f"Última Corrida: {race['race_name']} ({race['season']})")
    st.write(f"📍 {race['circuit_name']} - {race['location']['locality']}, {race['location']['country']}")
    st.write(f"📅 Data: {race['date']}")

    st.markdown("### 🏆 Top 3 Pilotos")
    for i, result in enumerate(race["results"][:3], 1):
        st.write(f"{i}º - {result['driver']} ({result['constructor']})")
except Exception as e:
    st.error("Erro ao carregar JSON da corrida.")
    st.exception(e)

# CSV
try:
    df = pd.read_csv(csv_path)
    st.markdown("## 📊 Resultados Gerais")

    corrida_escolhida = st.selectbox("Escolha uma corrida:", df['race_name'].unique())
    corrida_df = df[df['race_name'] == corrida_escolhida]

    st.dataframe(corrida_df[['position', 'driver', 'constructor', 'points']])

    st.bar_chart(corrida_df.set_index('driver')['points'])
except Exception as e:
    st.error("Erro ao carregar dados CSV.")
    st.exception(e)
