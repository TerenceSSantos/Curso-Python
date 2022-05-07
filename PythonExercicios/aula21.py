#   Funções parte 2

# Interactive Help
#   help()


#help()
help(print)
help(len)
print(print.__doc__)

# Docstrings: Texto de ajuda para ser utilizado no help(). Deve ser criado com 3 aspas duplas na linha abaixo do comando

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')

contador(10, 0, 3)
help(contador)

# Paramêtros opcionais

def somar(a=0, b=10, c=0):   # Caso os parâmetros não sejam informados, ele utilizará o valor padrão informado após o igual
    s = a + b + c
    print(f'A soma vale {s}')

print('=' * 60)
somar(3, 2, 5)
somar(8, 4)
somar()

# Escopo de variáveis
#
def teste(b):
    b += 4
    c = 2
    # a = 8 => desta forma estou criando um "a" local
    # global a => desta forma estou dizendo que o "a" é global
    print(f'a dentro vale {a}') # "a" é uma variável global.
    print(f'b vale {b} e c vale {c}')

print('=' * 60)
a = 100
teste(a)

# Retornando valores
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

print('=' * 60)
resp = somar(3, 2, 5)
print(f'a soma resultou em {resp}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

print('=' * 60)
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')


def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False

print('=' * 60)
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')