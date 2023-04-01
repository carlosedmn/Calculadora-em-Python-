import time
import math
from colorama import init, Fore, Style

init(autoreset=True)

# Define uma função para ler um número float


def ler_numero_float(mensagem):
    while True:
        try:
            numero = float(input(Fore.YELLOW + mensagem + ": "))
            return numero
        except ValueError:
            print(Fore.RED + "Valor inválido. Digite novamente." + Style.RESET_ALL)

# Define uma função para calcular as operações


def calcular(a, b, operador):
    if operador == "+":
        resultado = a + b
    elif operador == "-":
        resultado = a - b
    elif operador == "*":
        resultado = a * b
    elif operador == "/":
        if b == 0:
            print(
                Fore.RED + "Não é possível dividir por zero. Digite outro valor." + Style.RESET_ALL)
            return None
        else:
            resultado = a / b
    elif operador == "**":
        resultado = a ** b
    elif operador == "//":
        resultado = a // b
    elif operador == "%":
        resultado = a % b
    elif operador == "log":
        resultado = math.log(a, b)
    elif operador == "sin":
        resultado = math.sin(a)
    elif operador == "cos":
        resultado = math.cos(a)
    elif operador == "tan":
        resultado = math.tan(a)
    elif operador == "sqrt":
        resultado = math.sqrt(a)
    else:
        print(Fore.RED + "Operador inválido! Tente novamente." + Style.RESET_ALL)
        return None
    return resultado


# Imprime cabeçalho
print(Fore.GREEN + "="*20)
print("Calculadora!")
print(Fore.GREEN + "="*20)

# Lê a operação
opcoes_operacoes = {
    "+": "somar",
    "-": "subtrair",
    "*": "multiplicar",
    "/": "dividir",
    "**": "potência",
    "//": "divisão inteira",
    "%": "resto da divisão",
    "log": "logaritmo",
    "sin": "seno",
    "cos": "cosseno",
    "tan": "tangente",
    "sqrt": "raiz quadrada"
}

op_valida = False
while not op_valida:
    print(Fore.CYAN + "Qual operação você irá utilizar?" + Style.RESET_ALL)
    for operador, nome_operacao in opcoes_operacoes.items():
        print(Fore.YELLOW +
              f"{operador} Para {nome_operacao}" + Style.RESET_ALL)
    op = input(Fore.YELLOW + "Digite o operador: " + Style.RESET_ALL)
    if op in opcoes_operacoes:
        op_valida = True
    else:
        print(Fore.RED + "Operador inválido! Tente novamente." + Style.RESET_ALL)

# Lê os números
a = ler_numero_float("Digite o primeiro número")
b = None
while b is None:
    b = ler_numero_float("Digite o segundo número")
    if op == "/" and b == 0:
        print(Fore.RED + "Não é possível dividir por zero. Digite outro valor." + Style.RESET_ALL)
        b = None

# Realiza a operação escolhida
resultado = calcular(a, b, op)

# Imprime o resultado
print(Fore.GREEN + "="*20)
print("Resultado:", resultado)
print(Fore.GREEN + "="*20)

input("Pressione Enter para sair...")
time.sleep(3)
