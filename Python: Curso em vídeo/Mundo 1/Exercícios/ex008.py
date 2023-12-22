# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Insira uma medida (em metros): "))
centimetros = metros * 100
milimetros = metros * 1000
print("{} metros equivale a {:.0f} centímetros, ou {:.0f} milímetros".format(metros, centimetros, milimetros))
