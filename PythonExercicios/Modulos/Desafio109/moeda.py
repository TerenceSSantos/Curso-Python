def metade(n, f=False):
    resultado = n / 2
    if f:
        return moeda(resultado, True)
    else:
        return resultado

def dobro(n, f=False):
    resultado = n * 2
    if f:
        return  moeda(resultado, True)
    else:
        return resultado

def aumentar(n, p, f=False):
    resultado = n + ((n / 100) * p)
    if f:
        return moeda(resultado, True)
    else:
        return resultado

def diminuir(n, p, f=False):
    resultado = n - ((n / 100) * p)
    if f:
        return moeda(resultado, True)
    else:
        return resultado

def moeda(m,f=False):
    if f:
        return f'R$ {m:.2f}'.replace('.', ',')
    else:
        return m