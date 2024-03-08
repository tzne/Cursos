# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis",
            "estudar", "praticar", "trabalhar", "mercado", "programador",
            "futuro")

for palavra in palavras:
    print(f"\n{palavra} possui as vogais", end=' ')
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
