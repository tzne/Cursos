# Crie um programa que leia o nome completo de uma pessoa e mostre:
#  – O nome com todas as letras maiúsculas e minúsculas.
#  – Quantas letras ao todo (sem considerar espaços).
#  – Quantas letras tem o primeiro nome.

nome = input("Insira seu nome completo: ")

print("""Seu nome em maiúsculas é {}
Seu nome em minúsculas é {}
Seu nome possui {} letras
Seu primeiro nome possui {} letras""".format(nome.upper(), nome.lower(), len(nome.replace(' ', '')), len(nome.split()[0])))
