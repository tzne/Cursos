# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

numero = randint(0, 5)
tentativa = int(input(("Vou pensar em um número inteiro entre 0 e 5. Tente adivinhar: ")))

if (numero == tentativa):
    print("Você acertou!")
else:
    print("Você errou, eu pensei no número {}".format(numero))
