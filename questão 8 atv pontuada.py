import os
os.system("cls")

cd = str(input("Digite a cor do cd: "))

if cd == "verde":
    preco = 10
elif cd == "azul":
    preco = 20
elif cd == "amarelo":
    preco = 30
elif cd == "vermelho":
    preco = 40
else:
    print("Inválido")

print("Sua opção de cd: ", cd)
print ("Preço do cd: ", preco)