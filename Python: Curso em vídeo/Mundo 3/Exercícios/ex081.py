''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista. '''

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

lista_numeros.sort(reverse=True)

print(f"Foram digitados {len(lista_numeros)} números")
print(f"A lista em ordem decrescente é {lista_numeros}")
print("O número 5 está na lista" if (5 in lista_numeros) else "O número 5 não está na lista")
