def metade(n):
    resultado = n / 2
    return moeda(resultado)

def dobro(n):
    resultado = n * 2
    return  moeda(resultado)

def aumentar(n, p):
    resultado = n + ((n / 100) * p)
    return moeda(resultado)

def diminuir(n, p):
    resultado = n - ((n / 100) * p)
    return moeda(resultado)

def moeda(m):
    return f'R$ {m:.2f}'.replace('.', ',')