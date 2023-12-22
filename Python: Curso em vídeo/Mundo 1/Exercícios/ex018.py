# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

graus = float(input("Insira um ângulo, em graus: "))
angulo = radians(graus)

print("O seno de {:.2f} é {:.2f}".format(graus, sin(angulo)))
print("O cosseno de {:.2f} é {:.2f}".format(graus, cos(angulo)))
print("A tangente de {:.2f} é {:.2f}".format(graus, tan(angulo)))
