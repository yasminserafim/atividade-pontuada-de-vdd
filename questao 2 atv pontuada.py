import os
os.system("cls")

# ENTRADA
nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu sexo: "))
estado_civil = str(input("Digite seu estado civil: "))
feminino = "f"
masculino = "m"
r_estado_civil = "casada"

# PROCESSAMENTO
if sexo == "f" and "casada":
    tempo_de_casamento = int(input("Digite seu tempo de casamento (em anos): "))
else:
        tempo_de_casamento = "Não importa"

print("=== EXIBINDO DADOS ===")
print("Seu nome: ", nome)
print("Seu sexo: ", sexo)
print("Seu estado civil: ", estado_civil)
print("Tempo de casamento: ", tempo_de_casamento)