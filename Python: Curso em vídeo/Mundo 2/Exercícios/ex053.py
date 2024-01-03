# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = ''.join(input("Digite uma frase: ").strip().lower().split())
palindromo = False
tamanho = (len(frase) - 1)
inverso = ''

for i in range(tamanho, -1, -1):
    inverso += frase[i]

print("A frase é um palíndromo" if (inverso == frase) else "A frase não é um palíndromo")
