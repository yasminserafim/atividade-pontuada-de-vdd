import os
os.system("cls")

#ENTRADA
valor_produto = float(input("Digite o valor do produto: "))
prazo = 2
a_vista = 1
pagamento = int(input("Digite a opção de pagamento: "))

# PROCESSAMENTO
match pagamento:
    case 1:
        desconto = valor_produto * 0.10
        valor_final = valor_produto - desconto
        print("Valor do produto: ", valor_produto)
        print("Forma de pagamento: ", a_vista)
        print("Valor do desconto: ", desconto)
        print("Total a pagar: ", valor_final)
    case 2:
        numero_parcelas = int(input("Digite o número de parcelas (até 6x): "))
        if numero_parcelas > 6:
            print("Quantidade de parcelas inválida.")
            exit() #FIM DO PROGRAMA
        valor_final = valor_produto / numero_parcelas
        print("Valor do produto: ", valor_produto)
        print("Forma de pagamento: ", prazo)
        print("Quantidade de parcelas: ", numero_parcelas)
        print("Valor por parcela: ", valor_final)
        print("Total a prazo: ", valor_produto)







