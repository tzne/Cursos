# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

lista_palpites = []
palpite = []

print(40 * "-")
print("JOGOS PARA MEGA SENA".center(40))
print(40 * "-")

numero_palpites = int(input("Quantos jogos você quer que eu sorteie? "))

for i in range(1, numero_palpites+1):
    for c in range(0, 6):
        numero = randint(1, 60)

        while numero in palpite:  # checa se o número ja existe no palpite
            numero = randint(1, 60)

        palpite.append(numero)
        palpite.sort()

    print(f"Jogo {i}: {palpite}")

    lista_palpites.append(palpite[:])
    palpite.clear()

    sleep(1.5)

print(lista_palpites)
