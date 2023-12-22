# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Insira uma frase: ").strip().lower()
print("""A letra 'A' aparece {} vezes na frase
A primeira letra 'A' aparece na posição {}
A última letra 'A' aparece na posição {}""".format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))
