MINIMA = 12


def idade_permitida(idade):
    if idade > 100:
        return False
    return idade > MINIMA
