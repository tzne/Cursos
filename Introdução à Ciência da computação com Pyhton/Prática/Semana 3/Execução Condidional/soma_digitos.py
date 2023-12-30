# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

numero = int(input("Digite um número inteiro: "))
casas = len(str(numero))
digito = 0

soma = 0
contador = 1
while (casas > 0):
    digito = (numero // (10**(casas-1)))
    numero = numero - (digito*(10**(casas-1)))
    casas -= 1
    contador += 1
    soma += digito
print(soma)
