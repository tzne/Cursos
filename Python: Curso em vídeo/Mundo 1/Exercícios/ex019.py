# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import randint, choice

aluno1 = input("Insira o nome do primeiro aluno: ")
aluno2 = input("Insira o nome do segundo aluno: ")
aluno3 = input("Insira o nome do terceiro aluno: ")
aluno4 = input("Insira o nome do quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]

print("O aluno escolhido foi {}".format(lista[randint(0, 3)]))
print("O aluno escolhido foi {}".format(choice(lista)))
