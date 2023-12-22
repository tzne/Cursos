# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input("Em qual cidade você nasceu? ").split()
teste = cidade.lower().split()
print("santo" == teste[0])
