# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#  A) qual é o total gasto na compra.
#  B) quantos produtos custam mais de R$1000.
#  C) qual é o nome do produto mais barato

total = produtos1000 = 0
precoProdutoBarato = 0
produtoBarato = str()
i = 0

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preco do produto: R$"))

    if ((preco < precoProdutoBarato) or (i == 0)):
        produtoBarato = nome
        precoProdutoBarato = preco

    if (preco > 1000):
        produtos1000 += 1

    total += preco
    i += 1

    opcao = input("Deseja continuar? [S/N] ").strip().upper()[0]
    while (opcao not in "SN"):
        opcao = input("Opção inválida! Deseja continuar? [S/N]").strip().upper()[0]
    if (opcao == 'N'):
        break

print(f"""O total da compra foi R${total:.2f}
Temos {produtos1000} produtos custando mais de R$1000.00
O produto mais barato foi {produtoBarato} que custa R${precoProdutoBarato:.2f}""")
