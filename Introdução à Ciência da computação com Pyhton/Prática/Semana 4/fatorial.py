# Escreva um programa que receba um número natural n e imprima n fatorial na saída

n = int(input("Insira um número natural: "))
resultado = 1

if (n == 0):
    resultado = 1
else:
    while(n >= 1):
        resultado = resultado * n
        n -= 1
print(resultado)
