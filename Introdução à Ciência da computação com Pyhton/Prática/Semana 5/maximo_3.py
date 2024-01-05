# Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles

def maximo(x, y, z):
    while not(x <= y <= z):
        if (x > y):
            x, y = y, x
        elif (y > z):
            y, z = z, y
    return z

