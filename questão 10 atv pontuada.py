import os
os.system("cls")

print('''
=== Bem Vindo ao Posto de Gasolina ===
Combustível	Quantidade Vendida	Desconto por Litro
Álcool  -   Até 25 litros   -   10%
Álcool  -   Acima de 25 litros  -   20%
Gasolina    -   Até 25 litros   -   15%
Gasolina    -   Acima de 25 litros  -   30%

A = ALCOOL
G = GASOLINA
''')

combustivel = input("ALCOOL OU GASOLINA: ")
litros = int(input("Quantos litros: "))

if combustivel == "A" and litros <= 25:
    total = (3.79 * litros) * 0.1
elif combustivel == "A" and litros > 25:
    total = (3.79 * litros) * 0.2
if combustivel == "G" and litros <= 25:
    total = (6.59 * litros) * 0.15
if combustivel == "G" and litros > 25:
    total = (6.59 * litros) * 0.3
else: 
    print("Nada a relatar")

print("Total a pagar: ", total)

