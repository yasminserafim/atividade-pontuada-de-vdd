import os
os.system("cls")

print('''
FRUTA   - ATÉ 5KG - ACIMA DE 5KG
MORANGO - R$ 2,50 - R$ 2,20
MAÇÃ    - R$ 1,80 - R$ 1,50
''')

fruta = str(input("Digite sua opção de fruta: "))
kg = float(input("Digite quantos kg deseja:"))

# PROCESSAMENTO
if fruta == "maçã" and kg >= 5:
    preco = kg * 1.50
elif fruta == "maçã" and kg < 5:
    preco = kg * 1.80
elif fruta == "morango" and kg >= 5:
    preco = kg * 2.20
elif fruta == "morango" and kg < 5:
    preco = kg * 2.50
else:
    preco = "Invalido"

# VALOR TOTAL
if preco == 15 or kg >= 10:
    valor_total = preco * 0.10
else:
    valor_total = preco

# EXIBINDO VALORES
print("TOTAL:")
print(valor_total)
