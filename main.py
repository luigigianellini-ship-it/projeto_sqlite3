import funcoes
import sqlite3
from pathlib import Path
ROOT_DIR = Path(__file__).parent
DB_NAME = "sistema.bancario"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "sistema_bancario"
c = {
    "limpa": "\033[m",
    "erro": "\033[1;31m", #vermelho
    "sucesso": "\033[1;32m", #verde
    "alerta": "\033[1;33m", #amarelo
    "info": "\033[1;34m", #lilas
    "roxo": "\033[1;35m" #roxo mais pra rosa =/
}

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()
parametros = {
    "con": con,
    "cursor": cursor,
    "TABLE_NAME": TABLE_NAME
}

cursor.execute(f"""
               CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               saldo REAL)
            """)
con.commit()

while True:
    menu = funcoes.menu([
        "Cadastrar",
        "Sacar",
        "Depositar",
        "Exibir Valores",
        "Apagar Tabela",
        "Sair"
    ])
    match menu:
        case 1:
            nome = funcoes.cadastrar(**parametros)
            print(nome)
        case 2:
            funcoes.sacar(**parametros)
        case 3:
            funcoes.depositar(**parametros)
        case 4:
            try:
                exibir,nome = funcoes.exibir(**parametros)
                print(f"{c['sucesso']}{nome} tem um saldo de {exibir} reais{c['limpa']}")
            except:
                print(f"{c['erro']}Usuario nao cadastrado{c['limpa']}")
        case 5:
            funcoes.apagar_tabela(**parametros)
        case 6:
            print(f"{c['alerta']}Saindo...{c['limpa']}")
            break
        case _:
            print(f"{c['erro']}Opcao invalida!{c['limpa']}")

cursor.close()
con.close()