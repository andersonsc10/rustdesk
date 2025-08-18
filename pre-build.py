#!/usr/bin/env python3

import os
import subprocess
import sys

# --- Servidor Customizado ---
# Dados do servidor para compilação automática.
# Altere estes valores se o seu servidor mudar.
SERVER_HOST = "cloud.sc10.nl"
SERVER_API_URL = "https://cloud.sc10.nl"
SERVER_KEY = "DYr7u9MIFN2GcT4nNIHZLBxQJjbXNvNQplTxvUgQ6No="
# --------------------------

print(">>> Configurando variáveis de ambiente para o build customizado...")

# Define as variáveis de ambiente que serão lidas pelo compilador Rust
os.environ['RENDEZVOUS_SERVER'] = SERVER_HOST
os.environ['RS_RELAY_SERVER'] = SERVER_HOST
os.environ['RS_API_SERVER'] = SERVER_API_URL
os.environ['RS_KEY'] = SERVER_KEY

print(f"    Servidor de ID/Rendezvous: {os.environ['RENDEZVOUS_SERVER']}")
print(f"    Servidor Relay:            {os.environ['RS_RELAY_SERVER']}")
print(f"    Servidor API:              {os.environ['RS_API_SERVER']}")
print(f"    Chave Pública:             {os.environ['RS_KEY']}")
print(">>> Variáveis configuradas com sucesso.")

# Constrói o comando para chamar o build.py, repassando todos os argumentos
# que foram recebidos por este script (ex: --flutter)
command = ["python3", "build.py"] + sys.argv[1:]

print(f"\n>>> Executando o script de compilação principal: {' '.join(command)}\n")

# Executa o script de build principal
try:
    # O check=True garante que o script pare se o build.py falhar
    subprocess.run(command, check=True)
    print("\n>>> Build finalizado com sucesso!")
except subprocess.CalledProcessError as e:
    print(f"\n>>> O script de build falhou com o código de saída: {e.returncode}")
    sys.exit(e.returncode)
except FileNotFoundError:
    print("\n>>> Erro: O comando 'python3' não foi encontrado.")
    print(">>> Tente instalar o Python 3 ou garanta que ele esteja no seu PATH.")
    sys.exit(1)
except Exception as e:
    print(f"\n>>> Ocorreu um erro inesperado durante a compilação: {e}")
    sys.exit(1)