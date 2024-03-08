# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expressao = input("Digite a expressão")
abre_parenteses = fecha_parenteses = 0

for i in range(len(expressao)):
    if (expressao[i] == "("):
        abre_parenteses += 1
    elif (expressao[i] == ")"):
        fecha_parenteses += 1

if abre_parenteses == fecha_parenteses:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")
