# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

opcao = "s"
colegio = []
aluno = []
notas = []

while opcao not in "Nn":
    aluno.append(input("Nome: "))
    notas.append(float(input("Nota 1: ")))
    notas.append(float(input("Nota 2: ")))

    aluno.append(notas[:])
    colegio.append(aluno[:])

    aluno.clear()
    notas.clear()

    opcao = input("Quer continuar? [S/N] ")

print(40*"=")
print(f"{'Número':<10} {'Nome':<20} {'Média':<}")
print(40*"-")
for i in range(0, len(colegio)):
    media = ((colegio[i][1][0] + colegio[i][1][1]) / 2)
    print(f"{i:<10} {colegio[i][0]:<20} {media:<}")
print(40*"-")

nota_aluno = int()
while True:
    nota_aluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if nota_aluno == 999:
        break
    print(f"Notas de {colegio[nota_aluno][0]} são {colegio[nota_aluno][1]}")
