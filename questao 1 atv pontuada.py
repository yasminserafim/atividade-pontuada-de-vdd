import os
os.system("cls")

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite mais um número: "))

if numero1 + numero2 < numero3:
    print("A soma dos 2 primeiros números e menor que o terceiro.")
else:
    print("A soma dos 2 primeiros números e maior que o terceiro.")
