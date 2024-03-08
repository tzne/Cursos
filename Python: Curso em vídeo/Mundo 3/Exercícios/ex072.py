# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

extenso = ("zero", "um", "dois", "três", "quatro",
           "cinco", "seis", "sete", "oito", "nove",
           "dez", "onze", "doze", "treze", "quatorze",
           "quinze", "dezesseis", "dezessete", "dezoito", "dezenove",
           "vinte")

numero = int(input("Insira um número inteiro entre 0 e 20: "))

while ((numero > 20) or (numero < 0)):
    numero = int(input("Número inválido! Insira um número inteiro entre 0 e 20: "))

print(f"O número escolhido foi {extenso[numero]}")
