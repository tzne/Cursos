# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta

matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(input((f"Digite um valor para [{linha}, {coluna}]: ")))

print(60*"=")
for i in range(0, 3):
    for j in range(0, 3):
        print(f" [{matriz[i][j]:^5}] ", end='')
    print()
