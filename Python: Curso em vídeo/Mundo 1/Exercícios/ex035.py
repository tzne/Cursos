# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

lado1 = float(input("Insira primeiro lado do triângulo: "))
lado2 = float(input("Insira segundo lado do triângulo: "))
lado3 = float(input("Insira segundo lado do triângulo: "))
if ((lado1+lado2 > lado3) and (lado2+lado3 > lado1) and (lado1+lado3 > lado2)):
    print("O triângulo existe")
else:
    print("O triângulo não existe")
