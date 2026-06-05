c = {
    "limpa": "\033[m",
    "erro": "\033[1;31m", #vermelho
    "sucesso": "\033[1;32m", #verde
    "alerta": "\033[1;33m", #amarelo
    "info": "\033[1;34m", #lilas
    "roxo": "\033[1;35m" #roxo mais pra rosa =/
}
def leiaFloat(msg):
    while True:
        try:
            valor = input(msg).replace(",", ".")
            return float(valor)
        except (ValueError, TypeError):
            print(f"{c["erro"]}Digite apenas numeros!{c["limpa"]}")
            continue
def leiaInt(msg):
    try:
        return int(input(msg))
    except (ValueError, TypeError):
        print(f"{c["erro"]}Digite apenas numeros!{c["limpa"]}")
        return "erro"
        