# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela

lista = []

for i in range(0, 5):
    numero = int(input("Digite um valor: "))

    if (i == 0) or (numero > lista[-1]):
        lista.append(numero)
        print("Adicionado ao fim da lista")
    else:
        c = 0
        while c < len(lista):
            if numero <= lista[c]:
                lista.insert(c, numero)
                print(f"Valor adicionado na posição {c} da lista")
                break
            c += 1

print(lista)
