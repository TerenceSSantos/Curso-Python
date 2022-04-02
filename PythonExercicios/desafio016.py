from math import trunc

num = float(input('Digite um número real: '))
print('Mostrando somente a parte inteira do número {}'.format(trunc(num)))
print('Parte inteira {}'.format(int(num)))
# print('Parte inteira: {:.0f}'.format(num))  Assim está fazendo arredondamento