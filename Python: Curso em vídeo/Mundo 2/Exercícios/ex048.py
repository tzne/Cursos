# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0
contador = 0
for i in range(0, 500, 3):
    if (i % 2 != 0):
        soma += i
        contador += 1
print("A soma dos {} múltiplos ímpares de 3 de 0 a 500 é {}".format(contador, soma))
