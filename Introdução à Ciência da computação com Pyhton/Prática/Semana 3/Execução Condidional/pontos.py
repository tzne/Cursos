# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

# longe

# na saída. Caso o contrário, quando a distância for menor que 10, imprima

# perto

ponto1x = float(input("Insira a coordenada X do primeiro ponto: "))
ponto1y = float(input("Insira a coordenada Y do primeiro ponto: "))
ponto2x = float(input("Insira a coordenada X do segundo ponto: "))
ponto2y = float(input("Insira a coordenada Y do segundo ponto: "))

distancia = ((ponto1x - ponto2x)**2 + (ponto1y - ponto2y))**(1/2)

if (distancia >= 10):
    print("longe")
else:
    print("perto")
