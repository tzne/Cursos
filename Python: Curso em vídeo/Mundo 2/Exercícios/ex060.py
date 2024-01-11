# Faça um programa que leia um número qualquer e mostre o seu fatorial

numero = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1

while (numero < 0):
    print("O número deve ser maior ou igual a zero")
    numero = int(input("Digite um número para calcular seu fatorial"))

while (numero > 0):
    fatorial *= numero
    numero -= 1

print("O fatorial é {}".format(fatorial))
