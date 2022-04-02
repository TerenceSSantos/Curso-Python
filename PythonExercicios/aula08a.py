import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz arredondada para cima de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz arredondada para baixo de {} é igual a {}'.format(num, math.floor(raiz)))