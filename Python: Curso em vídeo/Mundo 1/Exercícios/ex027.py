# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = input("Insira seu nome completo: ").strip().split()
print("""Seu primeiro nome é {}
Seu último nome é {}""".format(nome[0], nome[len(nome)-1]))
