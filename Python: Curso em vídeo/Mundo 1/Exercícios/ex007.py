# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

print("A média entre {:.1f} e {:.1f} é {:.1f}".format(nota1, nota2, ((nota1+nota2)/2)))
