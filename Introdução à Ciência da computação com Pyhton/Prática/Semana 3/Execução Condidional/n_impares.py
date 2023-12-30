# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaix

n = int(input("Digite o valor de n: "))
i = 1
numero = 1

while (i <= n):
    if ((numero % 2) != 0):
        print(numero)
    i += 1
    numero += 2
