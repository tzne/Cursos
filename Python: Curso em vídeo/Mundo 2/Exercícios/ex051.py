# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

a1 = float(input("Insira o primeiro termo da PA: "))
razao = float(input("Insira a razao da PA: "))

for i in range(0, 10):
    print(a1 + (i*razao), end=' ')
