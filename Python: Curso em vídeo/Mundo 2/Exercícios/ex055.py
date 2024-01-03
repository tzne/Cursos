# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

pesado = float(input("Insira o peso da 1° pessoa: "))
leve = pesado

for pessoa in range(1, 5):
    peso = float(input("Insira o peso da {} pessoa: ".format(pessoa + 1)))

    if (peso >= pesado):
        pesado = peso
    elif (peso <= leve):
        leve = peso

print("O maior peso lido foi de {} e o maior peso lido foi de {}".format(pesado, leve))
