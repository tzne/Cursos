# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

numero = int(input("Digite um número inteiro: "))
i = 2
primo = True
if numero < 2:
    primo = False
while (i < int((numero**(1/2))) + 1):
    if numero % i == 0:
        primo = False
    i += 1
print("primo" if primo else "não primo")
