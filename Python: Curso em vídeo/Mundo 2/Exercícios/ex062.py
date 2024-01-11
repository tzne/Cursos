# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos

termo = a1 = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
c = 1
quantidadeTermos = 10
continuarPA = True
termos = 0

while (continuarPA):
    while (c <= quantidadeTermos):
        print("{} ".format(termo), end='')
        termo += razao
        c += 1
        termos += 1

    quantidadeTermos = int(input("\nDeseja exibir quantos termos mais? "))
    if (quantidadeTermos == 0):
        continuarPA = False
    c = 1


print("Progressão finalizada com {} termos mostrados".format(termos))
