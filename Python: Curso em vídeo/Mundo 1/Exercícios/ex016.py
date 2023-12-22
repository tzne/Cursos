# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
from math import trunc

numero = float(input("Insira um número real: "))
print("A parte inteira de {} é {}".format(numero, trunc(numero)))
print("A parte inteira de {} é {:.0f}".format(numero, numero))
print("A parte inteira de {} é {:.0f}".format(numero, int(numero)))
