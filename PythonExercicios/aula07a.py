n1 = int(input('Digite um valor: '))
n2 = int (input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end='') # end não quebra linha, no caso, colocará um espaço
print('Divisão inteira {} e potência {}' .format(di, e))