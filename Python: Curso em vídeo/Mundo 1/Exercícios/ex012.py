# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input("Insira o preço do produto sem reajuste: R$"))
print("Com o reajuste, o produto passará a custar R${:.2f}".format(preco*0.95))
