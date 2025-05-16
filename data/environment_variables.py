import os

from dotenv import find_dotenv, load_dotenv

# Buscar o arquivo .env na raiz do projeto
dotenv_path = find_dotenv()

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path)
