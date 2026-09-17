import os
os.system("cls")

print("=== Bem Vindo ao Posto de Gasolina ===")

combustivel = str(input("Digite sua opção de combustível: "))
litros = float(input("Digite quantos litros você vai querer: "))

if combustivel == "A":
    preco = 3.79
elif combustivel == "G":
    preco = 6.59
elif combustivel == "A" and litro <= 25:
    desconto = preco * 0.1
elif combustivel == "A" and litro > 25:
    desconto = preco * 0.2
elif combustivel == "G" and litro <= 25:
    desconto = preco * 0.15
elif combustivel == "G" and litro > 25:
    desconto = preco * 0.3
else:
    print("Inválido")

total = preco * litros
valor_total = total - desconto

print("=== NOTA FISCAL ===")
print("Sua opção de combustível: ", combustivel)
print("Quantidade de litros: ", litros)
print("Desconto: ", desconto)
print("Total: ", total)
print("Valor Total: ", valor_total)