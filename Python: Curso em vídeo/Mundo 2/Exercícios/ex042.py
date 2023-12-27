# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes


lado1 = float(input("Insira primeiro lado do triângulo: "))
lado2 = float(input("Insira segundo lado do triângulo: "))
lado3 = float(input("Insira segundo lado do triângulo: "))

if ((lado1+lado2 > lado3) and (lado2+lado3 > lado1) and (lado1+lado3 > lado2)):
    print("O triângulo PODE ser formado, e é ", end='')
    if (lado1 == lado2 == lado3):
        print("EQUILÁTERO")
    elif (lado1 != lado2 != lado3 != lado1):
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("O triângulo NÃO PODE ser formado")
