# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual o salário do funcionário? R$"))
salario = salario*1.1 if salario > 1250 else salario * 1.15
print("O salário reajustado será de R${:.2f}".format(salario))
