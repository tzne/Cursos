# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Insira um número inteiro: "))
escolha = input("""Escolha umaads bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: """)

if escolha == '1':
    conversao = bin(numero)[2:] # converte o número para binário, (0bxxxxxx), e remove os dois primeiros caracteres (0b)
    print("{} convertido para binário e igual a {}".format(numero, conversao))
elif escolha == '2':
    conversao = oct(numero)[2:]
    print("{} convertido para binário e igual a {}".format(numero, conversao))
elif escolha == '3':
    conversao = hex(numero)[2:]
    print("{} convertido para binário e igual a {}".format(numero, conversao))
else:
    print("Opção inválida")
