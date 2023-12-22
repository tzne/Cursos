# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Insira o número de dias referente ao aluguel: "))
distancia = float(input("Insira a distância percorrida durante o alguel: "))
total = dias*60 + distancia*0.15
print("O valor do aluguel fica R${:.2f}".format(total))
