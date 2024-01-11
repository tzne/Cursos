# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

numero = int(input("Insira um número inteiro: "))
contador = 1
soma = numero
maior = menor = numero
opcao = input("Deseja continuar? [s/N] ").strip().upper()

while (opcao.strip().upper() == "S"):
    numero = int(input("Insira um número inteiro: "))

    soma += numero
    contador += 1

    if (numero >= maior):
        maior = numero
    elif (numero <= menor):
        maior = numero

    opcao = input("Deseja continuar? [S/n] ").strip().upper()

print("""Você digitou {} números e a média foi {:.2f}
O maior valor digitado foi {} e o menor foi {}""".format(contador, (soma/contador), maior, menor))
