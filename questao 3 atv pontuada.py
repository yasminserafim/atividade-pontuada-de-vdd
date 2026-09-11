import os
os.system("cls")

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 == numero2:
    resultado = numero1 + numero2
else:
    resultado = numero1 * numero2

print("=== EXIBINDO RESULTADOS ===")
print(resultado)