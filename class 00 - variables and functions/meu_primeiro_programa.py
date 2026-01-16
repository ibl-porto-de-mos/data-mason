def soma(x, y):
    return x + y

def menos(x, y):
    return x - y

def bananinha(x, y):
    return x / y

def multiplicacao(x, y):
    return x * y

def expoente(base, expoente):
    resultado = (f"{base} * " * expoente)[:-3] 
    return eval(resultado)

def calculadora():
    operacao = input("operacao desejada: ").strip()

    operações_disponiveis = {
        "mais": soma,
        "menos": menos,
        "dividir": bananinha,
        "multiplicar": multiplicacao,
        "potencia": expoente
    }

    k = int(input("Insira um numero: "))
    w = int(input("Insira um segundo numero: "))

    resultado = operações_disponiveis[operacao](k, w)
    
    mensagem = f"{k} {operacao} {w} é: {resultado}"

    print(mensagem)


if __name__ == '__main__':
    calculadora()
