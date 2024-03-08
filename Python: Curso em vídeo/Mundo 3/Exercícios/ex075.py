# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#  A) Quantas vezes apareceu o valor 9.
#  B) Em que posição foi digitado o primeiro valor 3.
#  C) Quais foram os números pares.

numeros = (int(input("Insira um número: ")),
           int(input("Insira um número: ")),
           int(input("Insira um número: ")),
           int(input("Insira um número: ")))


print(f"O número 9 aparece {numeros.count(9)} vezes")

if 3 in numeros:
    print(f"O primeiro valor 3 foi está na {numeros.index(3) + 1}° posição")
else:
    print("O valor 3 não foi inserido")

print("Os números digitados foram ", end='')
for n in numeros:
    if (n % 2 == 0):
        print(n, end=' ')
