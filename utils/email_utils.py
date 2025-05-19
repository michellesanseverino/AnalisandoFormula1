from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER", "")
EMAIL_PASS = os.getenv("EMAIL_PASS", "")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "")

def send_daily_email(content):
    msg = MIMEText(content, "html")
    msg["Subject"] = "Resumo Diário da Fórmula 1"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

def generate_html_summary(last_race, next_race, top_drivers, top_constructors, stats):
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial; background: #f5f5f5; padding: 20px; }}
            h2 {{ color: #d32f2f; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; }}
            th {{ background-color: #eee; }}
        </style>
    </head>
    <body>
        <h2>🏁 Resumo Diário - Fórmula 1</h2>

        <h3>Última Corrida</h3>
        <p><strong>{last_race.get("race_name", "N/A")}</strong> - {last_race.get("date", "N/A")}</p>

        <h3>Próxima Corrida</h3>
        <p><strong>{next_race.get("race_name", "N/A")}</strong> - {next_race.get("date", "N/A")}</p>

        <h3>Top 5 Pilotos</h3>
        <table><tr><th>Posição</th><th>Nome</th><th>Pontos</th></tr>
    """
    for driver in top_drivers:
        html += f"<tr><td>{driver['position']}</td><td>{driver['name']}</td><td>{driver['points']}</td></tr>"

    html += "</table><h3>Top 5 Construtores</h3><table><tr><th>Posição</th><th>Equipe</th><th>Pontos</th></tr>"

    for team in top_constructors:
        html += f"<tr><td>{team['position']}</td><td>{team['name']}</td><td>{team['points']}</td></tr>"

    html += f"""
        </table>
        <h3>Status Atual</h3>
        <ul>
            <li><strong>Volta mais rápida:</strong> {stats.get("fastest_lap", "N/A")}</li>
            <li><strong>Pole Position:</strong> {stats.get("pole_position", "N/A")}</li>
        </ul>
        <p>Enviado em {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
    </body></html>
    """
    return html
