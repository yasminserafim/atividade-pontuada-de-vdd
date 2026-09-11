import os
os.system("cls")

# ENTRADA
print("=== CALCULANDO SEU PESO IDEAL ===")
masculino = "m"
feminino = "f"
genero = (input("Digite o seu gênero: "))
altura = float(input("Digite sua altura: "))

match genero:
    case "m":
        peso_ideal = (72.7 * altura) - 58
        print("Esse é seu peso ideal: ", peso_ideal)
    case "f":
        peso_ideal = (62.1 * altura) - 44.7
        print("Esse é seu peso ideal: ", peso_ideal)