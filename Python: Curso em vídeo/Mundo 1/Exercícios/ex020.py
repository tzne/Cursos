# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample,shuffle

aluno1 = input("Insira o nome do primeiro aluno: ")
aluno2 = input("Insira o nome do segundo aluno: ")
aluno3 = input("Insira o nome do terceiro aluno: ")
aluno4 = input("Insira o nome do quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]

print(lista)

print("A ordem de apresentação será {}".format(sample(lista, k=4)))
