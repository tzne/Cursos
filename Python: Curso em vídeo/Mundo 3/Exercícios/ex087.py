''' Aprimore o desafio anterior, mostrando no final:
  A) A soma de todos os valores pares digitados.
  B) A soma dos valores da terceira coluna.
  C) O maior valor da segunda linha '''

matriz = [[], [], []]
pares = []
soma_pares = 0
soma_terceira = 0
maior_segunda = int()

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input((f"Digite um valor para [{linha}, {coluna}]: "))))

print(60*"=")
for i in range(0, 3):
    for j in range(0, 3):
        print(f" [{matriz[i][j]:^5}] ", end='')
        if ((matriz[i][j] % 2) == 0):
            pares.append(matriz[i][j])
    print()

    soma_terceira += matriz[i][2]

    if maior_segunda <= matriz[1][i]:
        maior_segunda = matriz[1][i]

print(60*"=")

for i in range(0, len(pares)):
    soma_pares += pares[i]

print(f"A soma dos valores pares é {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma_terceira}")
print(f"O maior valor da sgunda linha é {maior_segunda}")
