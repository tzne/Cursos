# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci

n = int(input("Quantos termos deseja exibir? "))
termo_n_1 = 0
termo_n_2 = 1
c = 0

while (c <= n):
    if (c == 0):
        termo = 0
    elif (c == 1):
        termo = 1
    else:
        termo = termo_n_1 + termo_n_2
    print(termo, end=' ')
    c += 1
    termo_n_1, termo_n_2 = termo_n_2, termo
print('')
