# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# Farei este exercício com os meio apresentados até então no curso

numero1 = int(input("Insira o primeiro número"))
numero2 = int(input("Insira o segundo número"))
numero3 = int(input("Insira o segundo número"))

if (numero1 < numero2):
    if (numero2 < numero3):
        print("O menor número é {} e o maior número é {}".format(numero1, numero3))
    else:
        print("O menor número é {} e o maior número é {}".format(numero1, numero2))
else:
    if (numero1 < numero3):
        print("O menor número é {} e o maior número é {}".format(numero2, numero3))
    else:
        print("O menor número é {} e o maior número é {}".format(numero2, numero1))
