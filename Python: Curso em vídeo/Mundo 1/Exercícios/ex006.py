# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input("Insira um número inteiro: "))
print("O dobro de {} é {}".format(numero, (numero*2)))
print("O triplo de {} é {}".format(numero, (numero*3)))
print("A raiz quadrada de {} é {:.2f}".format(numero, (numero**(1/2))))
