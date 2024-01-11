# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

a1 = float(input("Insira o primeiro termo da PA: "))
razao = float(input("Insira a razão da PA: "))
c = 0

while (c < 10):
    print(a1 + c * razao, end=' ')
    c += 1
