# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

somaIdade = 0
maisVelho = 0
mulheres = 0

for pessoa in range(0, 4):
    print("{}° pessoa".format(pessoa+1))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()

    somaIdade += idade

    if ((sexo == 'M') and (idade > maisVelho)):
        homemMaisVelho = nome
        maisVelho = idade

    if ((sexo == 'F') and (idade < 20)):
        mulheres += 1

print("A média de idade do grupo é de {} anos".format(somaIdade/4))
print("O homem mais velho tem {} anos e se chama {}".format(maisVelho, homemMaisVelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(mulheres))
