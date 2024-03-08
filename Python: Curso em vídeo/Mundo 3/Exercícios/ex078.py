# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = menor = int()

for i in range(0, 5):
    numero = int(input(f"Digite um valor para a posição {i}: "))
    lista.append(numero)

    if i == 0:
        maior = menor = numero

    if numero >= maior:
        maior = numero

    if numero <= menor:
        menor = numero

posicoes_maior = []
posicoes_menor = []

for i in range(len(lista)):
    if lista[i] == maior:
        posicoes_maior.append(i)
for i in range(len(lista)):
    if lista[i] == menor:
        posicoes_menor.append(i)

print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} nas posições {posicoes_maior}")
print(f"O menor valor digitado foi {menor} nas posições {posicoes_menor}")
