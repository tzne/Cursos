# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))
i = 2
primo = True

if numero < 2:
    primo = False
for i in range(2, int((numero**(1/2))) + 1):
    if numero % i == 0:
        primo = False
    i += 1
print("primo" if primo else "não primo")
