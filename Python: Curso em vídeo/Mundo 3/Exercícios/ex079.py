# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

lista_numeros = []
opcao = "s"

while opcao not in "Nn":
    numero = int(input("Digite um valor: "))

    if numero not in lista_numeros:
        lista_numeros.append(numero)
        print("Valor adicionado à lista")
    else:
        print("Valor duplicado! Não será adicionado à lista")

    opcao = input("Deseja continuar? [S/N] ").lower()

lista_numeros.sort()

print(f"Você digitou os valores {lista_numeros}")
