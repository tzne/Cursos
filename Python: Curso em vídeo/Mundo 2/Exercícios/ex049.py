# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input("Insira um número inteiro para conferir sua tabuada: "))

for i in range(0, 11):
    print("{} x {:>2} = {}".format(numero, i, numero*i))
