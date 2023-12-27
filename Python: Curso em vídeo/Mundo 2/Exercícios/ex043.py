# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida

peso = float(input("Insira sua massa, em kg: "))
altura = float(input("Insira sua altura, em metros: "))
imc = peso / (altura ** 2)

if (imc < 18.5):
    print("Abaixo do peso (IMC = {:.1f})".format(imc))
elif (18.5 < imc <= 25):
    print("Peso ideal (IMC = {:.1f})".format(imc))
elif (25 < imc <= 30):
    print("Sobrepeso (IMC = {:.1f})".format(imc))
elif (30 < imc <= 40):
    print("Obesidade (IMC = {:.1f})".format(imc))
else:
    print("Obesidade mórbida (IMC = {:.1f})".format(imc))
