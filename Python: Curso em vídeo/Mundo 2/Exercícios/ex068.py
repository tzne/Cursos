# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

print("Vamos jogar par ou ímpar")
vitoriasJogador = 0

while True:
    numeroJogador = int(input("Digite um valor: "))
    numeroComputador = randint(0, 10)
    numeroSoma = numeroJogador + numeroComputador
    par = ((numeroSoma % 2) == 0)

    jogada = input("Par ou Ímpar [P/I]? ").strip().upper()

    print(f"{6*' '}Você jogou {numeroJogador} e o computador jogou {numeroComputador}")
    print(f"{6*' '}Total: {numeroSoma} ({'PAR' if par else 'ÍMPAR'})")

    if ((jogada == 'P') and ((numeroSoma % 2) == 0)) or ((jogada == 'I') and ((numeroSoma % 2) != 0)):
        print(f"{6*' '}Você VENCEU!")
        vitoriasJogador += 1
    else:
        print(f"{6*' '}Você PERDEU!")
        break

print(f"Game Over! Você venceu {vitoriasJogador} vezes"
      if (vitoriasJogador != 0)
      else "Game Over! Você não teve nenhuma vitória")
