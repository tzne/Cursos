# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

numero = int(input("Insira um número inteiro: "))
if (numero%2 == 1):
    print("{} é ímpar".format(numero))
else:
    print("{} é par".format(numero))
