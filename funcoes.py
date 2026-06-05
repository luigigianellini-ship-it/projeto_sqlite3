import ler_num
import sqlite3
c = {
    "limpa": "\033[m",
    "erro": "\033[1;31m", #vermelho
    "sucesso": "\033[1;32m", #verde
    "alerta": "\033[1;33m", #amarelo
    "info": "\033[1;34m", #lilas
    "roxo": "\033[1;35m" #roxo mais pra rosa =/
}
def buscar(con,cursor,TABLE_NAME, nome):
    cursor.execute(f"""
        SELECT id FROM {TABLE_NAME} WHERE nome = ?
    """, (nome,))
    resultado = cursor.fetchone()
    if resultado is not None:
        return "existe"
    else:
        return f"{c['erro']}Usuario nao cadastrado{c['limpa']}"
def cadastrar(con, cursor, TABLE_NAME):
    nome = input(f"{c['info']}Digite o nome: {c['limpa']}").title().strip()
    verificar = buscar(con,cursor,TABLE_NAME, nome)
    if verificar == "existe":
        return f"{c['alerta']}Usuario ja cadastrado!{c['limpa']}"
    else:
        saldo = ler_num.leiaFloat(F"{c['info']}Digite o seu saldo: {c['limpa']}")
        sql = f"INSERT INTO {TABLE_NAME} (nome, saldo) VALUES (?, ?)"
        cursor.execute(sql, (nome, saldo))
        con.commit()
        return f"{c['sucesso']}{nome} cadastrado com sucesso!{c['limpa']}"

def sacar(con, cursor, TABLE_NAME):
    nome = input(f"{c['info']}Digite o nome: {c['limpa']}").title().strip()
    verificar = buscar(con, cursor, TABLE_NAME, nome)
    if verificar == "existe":
        saque = ler_num.leiaFloat(f"{c['info']}Valor do saque: {c['limpa']}")
        cursor.execute(f"SELECT saldo FROM {TABLE_NAME} WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()[0]
        resultado -= saque
        sql = f"""
UPDATE {TABLE_NAME}
SET saldo = ?
WHERE nome = ?;
        """
        cursor.execute(sql, (resultado,nome,))
        con.commit()
        print(f"{c['sucesso']}Saque realizado com sucesso!{c['limpa']}")
def depositar(con, cursor, TABLE_NAME):
    nome = input(f"{c['info']}Digite o nome: {c['limpa']}").title().strip()
    verificar = buscar(con, cursor, TABLE_NAME, nome)
    if verificar == "existe":
        deposito= ler_num.leiaFloat(f"{c['info']}Valor do deposito: {c['limpa']}")
        cursor.execute(f"SELECT saldo FROM {TABLE_NAME} WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()[0]
        resultado += deposito
        sql = f"""
UPDATE {TABLE_NAME}
SET saldo = ?
WHERE nome = ?;
        """
        cursor.execute(sql, (resultado,nome,))
        con.commit()
        print(f"{c['sucesso']}Deposito realizado com sucesso!{c['limpa']}")
def apagar_tabela(con,cursor, TABLE_NAME):
    while True:
        quest = input("Apagar um usuario especifico?(S/N): ").lower().strip()
        if quest not in ("s", "n"):
            print(f"{c["erro"]}Opcao invalida!{c['limpa']}")
            continue
        else:
            break
    if quest == "n":
        cursor.execute(f"DELETE FROM {TABLE_NAME}")
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name = '{TABLE_NAME}'",)
        print(f"{c['sucesso']}Tabela apagada!{c['limpa']}")
        con.commit()
    else:
        nome = input("Nome para excluir: ").title().strip()
        busca = buscar(con,cursor,TABLE_NAME,nome)
        if busca == "existe":
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE nome = ?",
                        (nome,))
            con.commit()
            print(f"{c['sucesso']}Usuario {nome} removido!{c['limpa']}")
        else:
            print(busca)
def exibir(con, cursor, TABLE_NAME):
    nome = input(f"{c['info']}Digite o nome para busca: {c['limpa']}").title().strip()
    resultado = buscar(con,cursor,TABLE_NAME,nome)
    if resultado == "existe":
        cursor.execute(f"""
    SELECT saldo FROM {TABLE_NAME} WHERE nome = ?
                    """, (nome,))
        return cursor.fetchone()[0],nome
    else:
        return resultado
def linha(tam = 50):
    print(f"{"-" * tam}")

def cabecalho(msg, tam=50):
    linha()
    print(f"{msg}".center(tam))
    linha()

def menu(lista):
    while True:
        try:
            cabecalho("MENU PRINCIPAL")
            contador = 1
            for item in lista:
                print(f"{c["alerta"]}{contador}{c["limpa"]} -  {c["roxo"]}{item}{c["limpa"]}")
                contador += 1
            opcao = ler_num.leiaInt("Sua opcao: ")
            if opcao == "erro":
                continue
            else:
                return opcao
        except KeyboardInterrupt:
            print(f"{c['erro']}Erro, acao cancelada pelo usuario{c['limpa']}")
            exit()
        except:
            print(f"{c['erro']}Erro, tente novamente{c['limpa']}")
            continue