''' 'Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
  A) Quantas pessoas foram cadastradas.
  B) Uma listagem com as pessoas mais pesadas.
  C) Uma listagem com as pessoas mais leves. '''

pessoa = []
lista = []
magros = []
gordos = []
opcao = "s"
quantidade = 0

while opcao not in "Nn":
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Peso: ")))

    if quantidade == 0:
        pesado = leve = pessoa[1]
    elif pessoa[1] >= pesado:
        pesado = pessoa[1]
    elif pessoa[1] <= leve:
        leve = pessoa[1]

    quantidade += 1
    lista.append(pessoa[:])

    pessoa.clear()

    opcao = input("Deseja continuar? [S/N] ").strip()

for i in range(0, quantidade):
    if lista[i][1] == leve:
        magros.append(lista[i][0])
    elif lista[i][1] == pesado:
        gordos.append(lista[i][0])

print(30*"=")
print(f"Ao todo, você cadastrou {quantidade} ({len(lista)}) pessoas")
print(f"O maior peso foi de {pesado}. Peso de {gordos}")
print(f"O menor peso foi de {leve}. Peso de {magros}")
