# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

lista_numeros = []
lista_pares = []
lista_impares = []
opcao = "s"

while opcao not in "Nn":
    numero = int(input("Digite um valor: "))
    lista_numeros.append(numero)

    if ((numero % 2) == 0):
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

    opcao = input("Deseja continuar? [S/N] ").lower()

print(f"Você digitou os valores {lista_numeros}")
print(f"A lista de pares é {lista_pares}")
print(f"A lista de ímpares é {lista_impares}")
