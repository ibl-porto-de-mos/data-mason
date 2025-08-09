def soma(x, y):
    return x + y

def menos(x, y):
    return x - y

def bananinha(x, y):
    return x / y

def cabecao(x, y):
    return x * y

def calculadora():
    operacao = input("operacao desejada: ")

    operações_disponiveis = {"mais": soma, "menos": menos, "dividir": bananinha, "multi": cabecao}

    k = int(input("Insira um numero: "))
    w = int(input("Insira um segundo numero: "))

    resultado = operações_disponiveis[operacao](k, w)
    
    mensagem = f"{k} {operacao} {w} é: {resultado}"

    print(mensagem)


if __name__ == '__main__':
    calculadora()


