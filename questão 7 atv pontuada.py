import os
os.system("cls")

produto = str(input("Digite seu produto: "))
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço unitário do produto: "))
total = quantidade * preco

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade > 5:
    desconto = total * 0.03
elif quantidade > 10:
    desconto = total * 0.05
else:
    print("Não se aplica")

total_pagar = total - desconto

print("Seu total: ", total)
print("Seu desconto: ", desconto)
print("Seu total a pagar: ", total_pagar)