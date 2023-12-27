# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

opcoes = ["PEDRA", "PAPEL", "TESOURA"]

jogada_computador = randint(0,2)
jogada_usuario = int(input("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Sua opção: """))

if (jogada_computador == jogada_usuario):
    print("Empatamos! Eu joguei {} e você jogou {}".format(opcoes[jogada_computador], opcoes[jogada_usuario]))
elif ((jogada_computador == 0) and (jogada_usuario == 1)) or ((jogada_computador == 1) and (jogada_usuario == 2)) or ((jogada_computador == 2) and jogada_usuario == 0):
    print("Eu perdi! Eu joguei {}, e você jogou {}".format(opcoes[jogada_computador], opcoes[jogada_usuario]))
else:
    print("Eu ganhei! Eu joguei {}, e você jogou {}".format(opcoes[jogada_computador], opcoes[jogada_usuario]))
