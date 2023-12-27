# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal

# – 3x ou mais no cartão: 20% de juros

preco = float(input("Qual o preço das compras? R$"))
pagamento = input("""FORMAS DE PAGAMENTO
[ 1 ] à vista (dinheiro/cheque)
[ 2 ] à vista (cartão)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Insira sua opção: """)

if pagamento == '1':
    print("Com um desconto de 10%, sua compra ficou em R${:.2f}".format(preco*0.9))
elif pagamento == '2':
    print("Com um desconto de 5%, sua compra ficou em R${:.2f}".format(preco*0.95))
elif pagamento == '3':
    print("Sua compra de R${:.2f} foi dividida em 2 parcelas de R{:.2f}".format(preco, preco/2))
elif pagamento == '4':
    parcelas = int(input("Em quantas parcelas será feiro o pagamento? "))
    print("Sua compra de R${:.2f} foi dividida em {} parcelas de {:.2f}, com juros aplicados".format(preco, parcelas, preco*1.2/parcelas))
else:
    print("Opção inválida")
