# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano_nascimento = int(input("Insira o ano em que nasceu: "))
ano_atual = date.today().year

if (ano_atual - ano_nascimento < 18):
    ano_alistamento = 18 - (ano_atual - ano_nascimento)
    print("Você ainda não precisa se alistar, precisará apenas daquia a {} anos".format(ano_alistamento))
elif (ano_atual - ano_nascimento == 18):
    print("Você precisa se alistar esse ano")
else:
    ano_alistamento = ano_atual - (ano_nascimento + 18)
    print("Você deveria ter se alistado há {} anos".format(ano_alistamento))
