# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

numeros = [[], []]

for i in range(1, 8):
    numero = int(input(f"Insira o {i}° valor: "))
    if ((numero % 2) == 0):
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()

print(60*"=")
print(f"Os valores pares digitados foram: {numeros[0]}")
print(f"Os valores ímpares digitados foram: {numeros[1]}")
