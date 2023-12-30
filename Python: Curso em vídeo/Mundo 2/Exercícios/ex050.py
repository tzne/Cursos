#  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0

for i in range(0, 6):
    numero = int(input("Insira um número inteiro: "))
    if ((numero % 2) == 0):
        soma += numero
        contador += 1
print("A soma dos {} números pares é {}".format(contador, soma))
