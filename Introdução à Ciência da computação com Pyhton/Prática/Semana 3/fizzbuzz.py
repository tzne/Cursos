# Receba um número inteiro na entrada e imprima

# FizzBuzz

# na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input("Insira um número inteiro: "))

print("FizzBuzz" if (((numero % 5) == 0) and (numero % 3) == 0) else numero)
