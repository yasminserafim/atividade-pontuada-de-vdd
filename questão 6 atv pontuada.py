import os
os.system("cls")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
print("Sua média: ", media)

if media >= 6:
    print("Aprovado!")
elif media >= 4.1:
    print("Recuperação")
else:
    print("Reprovado")
