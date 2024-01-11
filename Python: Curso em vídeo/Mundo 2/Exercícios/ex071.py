# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

total50 = total20 = total10 = total1 = valor = 0
valor = int(input("Qual valor deseja sacar? "))  # dinheiro é float, porém o exercío só devolveria quantias inteiras

while (valor > 1):

    while (valor >= 50):
        total50 += 1
        valor -= 50

    while (valor >= 20):
        total20 += 1
        valor -= 20

    while (valor >= 10):
        total10 += 1
        valor -= 10

    while (valor >= 1):
        total1 += 1
        valor -= 1


print(f"Total de {total50} células de R$50" if (total50 != 0) else '')
print(f"Total de {total20} células de R$20" if (total20 != 0) else '')
print(f"Total de {total10} células de R$10" if (total10 != 0) else '')
print(f"Total de {total1} células de R$1" if (total1 != 0) else '')
