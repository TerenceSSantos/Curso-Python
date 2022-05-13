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

def resumo(preco, acresc, desc):
    print('=' * 60)
    print(f'{"RESUMO DO VALOR":^60}')
    print('=' * 60)
    print(f'{"Preço analisado:":.<20}{moeda(preco, True):.>12}')
    print(f'{"Dobro do preço:":.<20}{dobro(preco, True):.>12}')
    print(f'{"Metade do preço:":.<20}{metade(preco, True):.>12}')
    print(f'{acresc}{"% de aumento:":.<18}{aumentar(preco, acresc, True):.>12}')
    print(f'{desc}{"% de desconto:":.<18}{diminuir(preco, desc, True):.>12}')