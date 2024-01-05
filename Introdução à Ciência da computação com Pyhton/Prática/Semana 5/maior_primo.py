# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

def primo(numero):
    if (numero <= 1):
        return False
    elif (numero <= 3):
        return True
    for i in range(2, int(numero**(1/2)) + 1):
        if numero % i == 0:
            return False
    return True

def maior_primo(numero):
    while numero >= 2:
        if primo(numero):
            return numero
        numero -= 1
