def fatorial(x):
    fat = 1
    while (x > 1):
        fat = fat * x
        x -= 1
    return fat

def testaFatorial():
    if (fatorial(1) == 1):
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if (fatorial(2) == 2):
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if (fatorial(0) == 1):
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if (fatorial(5) == 120):
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

def numeroBinomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))
