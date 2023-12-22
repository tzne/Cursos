# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
# from math import sqrt
from math import hypot

cateto1 = float(input("Insira o comprimento do primeiro cateto: "))
cateto2 = float(input("Insira o comprimento do segundo cateto: "))
# hipotenusa = sqrt(cateto1**2 + cateto2**2)
hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
# hipotenusa = hypot(cateto1, cateto2)

print("A hipotenusa é {}".format(hipotenusa))
