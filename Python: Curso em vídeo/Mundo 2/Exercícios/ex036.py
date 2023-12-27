# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

valor = float(input("Insira o valor da casa: R$"))
salario = float(input("Insira seu salário: R$"))
anos = float(input("Em quantos anos a casa será paga? "))

mensalidade = valor / (anos * 12)
print("A mensalidade será de R${:.2f} mensais".format(mensalidade))

if (mensalidade >= (salario * 0.3)):
    print("O empréstimo foi negado")
else:
    print("O empréstimo foi aprovado")
