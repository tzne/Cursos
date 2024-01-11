# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint

numero = randint(0, 10)
tentativas = 1

print("""Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")

palpite = int(input("Qual o seu palpite? "))

while (palpite != numero):
    if (palpite < numero):
        print("Mais... Tente mais uma vez")
    elif (palpite > numero):
        print("Menos... Tente mais uma vez")

    palpite = int(input("Qual o seu palpite? "))

    tentativas += 1

print("Acertou com {} tentativas".format(tentativas))
