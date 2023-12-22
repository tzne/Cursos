# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

real = float(input("Quanto dinheiro você tem na carteira? R$"))
print("Com R${:.2f} você pode comprar ${:.2f}".format(real, (real/4.86)))
