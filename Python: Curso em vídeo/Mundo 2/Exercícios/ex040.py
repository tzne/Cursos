# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
media = (nota1 + nota2) / 2

if (media < 5):
    print("O aluno foi REPROVADO, com nota {:.1f}".format(media))
elif (media >= 7):
    print("O aluno foi APOVADO, com nota {:.1f}".format(media))
else:
    print("O aluno está de recuperação, com nota {:.1f}".format(media))
