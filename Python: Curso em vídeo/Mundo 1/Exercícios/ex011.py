# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

altura = float(input("Insira, em metros, a altura da parede: "))
largura = float(input("Insira, em metros, a largura da parede: "))
area = altura * largura

print("A parede possui {}m², portanto será preciso {} litros de tinta".format(area, (area/2)))
