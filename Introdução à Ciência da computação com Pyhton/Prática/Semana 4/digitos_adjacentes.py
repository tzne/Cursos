# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

numero = input("Digite um número inteiro: ")
tamanho = len(numero)
i = 0
adjacente = False

while (i+1 != tamanho):
    if (numero[i] == numero[i+1]):
        adjacente = True
    i += 1

print("sim" if adjacente else "não")
