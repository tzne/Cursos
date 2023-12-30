# Faça um programa que aceite os coeficientes de uma equação segundo grau e calcúle suas raízes quadradas

from math import sqrt

a = float(input("Insira o coeficiente 'a' da equação: "))
b = float(input("Insira o coeficiente 'b' da equação: "))
c = float(input("Insira o coeficiente 'c' da equação: "))

delta = b**2 - 4 * a * c

if (delta < 0):
    print("esta equação não possui raízes reais")
elif (delta == 0):
    print("a raiz desta equação é {}".format((-b) / (2 * a)))
else:
    raiz1 = ((-b) + sqrt(b**2 - (4 * a * c))) / (2 * a)
    raiz2 = ((-b) - sqrt(b**2 - (4 * a * c))) / (2 * a)
    if (raiz1 < raiz2):
        print("as raízes da equação são {} e {}".format(raiz1, raiz2))
    else:
        print("as raízes da equação são {} e {}".format(raiz2, raiz1))
