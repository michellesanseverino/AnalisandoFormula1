# F1 Insights Automator

⚠️ **Projeto em progresso, portanto este README será atualizado com mais informações**

Um sistema RPA em Python que automatiza a coleta, organização e análise de dados da Fórmula 1, entregando painéis, alertas, relatórios e comparações de desempenho de forma inteligente e visual.

## Objetivos
1. Agenda RPA → `main.py`
2. Coleta dados com `fetch_data.py`
3. Salva arquivos locais (JSON/CSV)
4. Gera:
   - Dashboard diário → `dashboard.py`
   - Relatórios históricos → `report_generator.py`
   - Alerta de mudanças → `classify_alert.py`
   - Comparação entre pilotos → `performance_comparator.py`
5. Envia e-mails automáticos (SMTP)
6. Organiza tudo em pastas (data/reports)

## Tecnologias e Bibliotecas

| Função                   | Ferramentas Sugeridas                                 |
| ------------------------ | ----------------------------------------------------- |
| Coleta de dados          | `requests`, `BeautifulSoup`, `Selenium`, `Ergast API` |
| Processamento de dados   | `pandas`, `datetime`, `openpyxl`                      |
| Visualização             | `matplotlib`, `seaborn`, `plotly`, `streamlit`        |
| Exportação               | `xlsxwriter`, `reportlab`, `PyPDF2`                   |
| Automação e agendamento  | `schedule`, `time`, `dotenv`, `smtplib`, `email.mime` |
| Interface Web (opcional) | `Flask` ou `Streamlit`                                |
| Git e Controle de Versão | GitHub + Git                                          |


## Estrutura de Pastas

```console
f1-insights-automator/
│
├── data/                       # Armazena arquivos CSV, Excel, JSON
├── reports/                    # Relatórios gerados
├── scripts/                    # Scripts principais
│   ├── fetch_data.py           # Coleta dados da API e sites
│   ├── classify_alert.py       # Compara classificação e envia alerta
│   ├── report_generator.py     # Gera relatórios em Excel/PDF
│   ├── performance_comparator.py # Compara desempenho entre pilotos
│   └── dashboard.py            # Gera/resume painel diário
│
├── utils/                      # Funções reutilizáveis
│   ├── api_utils.py
│   ├── email_utils.py
│   └── plotting.py
│
├── .env                        # Segredos (e-mail, senhas, chaves)
├── requirements.txt
└── main.py                     # Orquestrador do projeto (agenda RPA)
```

## Funcionalidades Detalhadas
1. Dashboard Diário Automatizado
    - Última corrida
    - Top 5 pilotos e construtores
    - Próxima corrida
    - Status atual (voltas rápidas, pole position)
    - Envio diário por e-mail (smtplib)

2. Gerador de Relatórios Históricos
    - Input: ID da corrida (ou temporada completa)
    - Saída: .xlsx com:
        - Grid de largada x chegada
        - Posições por volta (se disponível)
        - Clima, tempos, etc.
    - Exportação para PDF (extra)

3. Alerta de Mudança na Classificação
    - Roda diariamente
    - Compara última classificação com versão salva
    - Se mudou, envia e-mail destacando as alterações
    - Usa difflib ou pandas.compare

4. Organizador de Dados da Temporada
    - Cria planilha com:
        - Corridas concluídas
        - Pontuação acumulada
        - Abas para cada piloto, construtor, etc.

5. Comparador de Desempenho entre Pilotos
    - Input: Nome dos dois pilotos
    - Compara:
        - Vitórias, pontos, posições médias
        - Tempo de qualificação
        - Voltas mais rápidas
    - Exibe com matplotlib ou streamlit