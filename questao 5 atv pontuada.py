import os
os.system("cls")

multiplicacao = "*"
adicao = "+"
subtracao = "-"
divisao = "/"

operacao = str(input("Digite um código de operação: "))
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

match operacao:
    case "*":
        resultado = numero1 * numero2
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "/":
        resultado = numero1 / numero2
    case _:
        resultado = "inválido"

print("=== EXIBINDO RESULTADO ===")
print(resultado)