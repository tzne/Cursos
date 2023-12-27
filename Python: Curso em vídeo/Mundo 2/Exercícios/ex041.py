# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM

# – Até 14 anos: INFANTIL

# – Até 19 anos: JÚNIOR

# – Até 25 anos: SÊNIOR

# – Acima de 25 anos: MASTER


from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Insira o ano de nascimento do atleta: "))

idade = ano_atual - ano_nascimento

if (idade <= 9):
    print("O atleta pertence à categoria MIRIM")
elif (9 < idade <= 14):
    print("O atleta pertence à categoria INFANTIL")
elif (14 < idade <= 19):
    print("O atleta pertence à categoria JÚNIOR")
elif (19 < idade <= 25):
    print("O atleta pertence à categoria SÊNIOR")
else:
    print("O atleta pertence à categoria MASTER")
