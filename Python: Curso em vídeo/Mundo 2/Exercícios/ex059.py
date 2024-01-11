# Crie um programa que leia dois valores e mostre um menu na tela:
#   [ 1 ] somar
#   [ 2 ] multiplicar
#   [ 3 ] maior
#   [ 4 ] novos números
#   [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
escolha = 0

while (escolha != 5):
    escolha = int(input("""{}
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    Qual a sua opção? """.format(30*'=')))

    if (escolha == 1):
        print("{} + {} = {}".format(valor1, valor2, valor1 + valor2))
    elif (escolha == 2):
        print("{} x {} = {}".format(valor1, valor2, valor1 * valor2))
    elif (escolha == 3):
        print("{} é o maior valor".format(valor1 if (valor1 >= valor2) else valor2))
    elif (escolha == 4):
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
    elif (escolha == 5):
        print("Programa finalizado")
    else:
        print("Opção inválida. Tente novamente")
