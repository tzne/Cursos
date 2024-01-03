# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

maiores = 0
ano_atual = date.today().year

for i in range(0, 7):
    ano_nascimento = int(input("Insira o ano em que a {}° pessoa nasceu: ".format( i + 1)))

    if ((ano_atual - ano_nascimento) >= 18):
        maiores += 1

print("Ao todo tivemos {} maiores de idade e {} menores de idade".format(maiores, (7 - maiores)))
