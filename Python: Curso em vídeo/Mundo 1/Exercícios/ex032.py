# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input("Insira um ano (0 para o ano atual): "))
if (ano == 0):
    ano = date.today().year
ano_4 = (ano % 4 != 0)
ano_100_400 = ((ano % 100 == 0) and (ano % 400 != 0))
if (ano_4 or ano_100_400):
    print("{} não é bissexto".format(ano))
else:
    print("{} é bissexto".format(ano))
