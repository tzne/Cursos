# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#  A) quantas pessoas tem mais de 18 anos.

#  B) quantos homens foram cadastrados.

#  C) quantas mulheres tem menos de 20 anos

maiores = homens = mulheres20 = 0

while True:
    idade = int(input("Insira a idade: "))

    sexo = input("Insira o sexo [M/F]: ").strip().upper()[0]
    while (sexo not in "MF"):
        sexo = input("Sexo inválido! Insira o sexo [M/F]: ").strip().upper()[0]

    if (idade > 18):
        maiores += 1

    if (sexo == 'M'):
        homens += 1

    if ((sexo in "Ff") and (idade < 20)):
        mulheres20 += 1

    opcao = input("Deseja continuar? [S/N] ").strip().upper()[0]
    while (opcao not in "SN"): 
        opcao = input("Opção inválida! Deseja continuar? [S/N] ").strip().upper()[0]
    if (opcao == 'N'):
        break

print(f"""Total de pessoas com mais de 18 anos: {maiores}
Ao todo temos {homens} homens cadastrados
E temos {mulheres20} mulheres com menos de 20 anos""")
