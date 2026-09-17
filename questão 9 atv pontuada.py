import os 
os.system("cls")

print("=== Bem Vindo a Financeira ===")
renda = float(input("Digite sua renda mensal: "))
emprestimo = float (input("Digite o valor do emprestimo: "))
prestacao = int(input("Digite os valores das prestações: "))


if emprestimo != renda * 10 and prestacao > (renda * 0.3):
    print("Emprestimo não aceito")
else:
    print("Emprestimo aceito")


