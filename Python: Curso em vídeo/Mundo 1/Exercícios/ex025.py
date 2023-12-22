# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome

nome = input("Insira seu nome: ").strip().lower()
print("Seu nome tem Silva? {}".format('silva' in nome))
