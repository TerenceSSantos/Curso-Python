#   Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

print('{:=^60}'.format(' COM FOR '))
fator = int(input('Digite um valor para fatorar: '))
resultado = 1
impressao = str(fator)
for i in range(fator, 1, -1):
    resultado = resultado * i
    impressao = impressao + ' x ' + str(i-1)
print(fator,end='! = '+ impressao)
print(' =', resultado)

# COM WHILE
print('{:=^60}'.format(' COM WHILE '))
fator = int(input('Digite um valor para fatorar: '))
resultado = 1
impressao = str(fator) + '! = '
while fator >= 1:
    resultado = resultado * fator
    if fator == 1:
        impressao = impressao + str(fator)
    else:
        impressao = impressao + str(fator) + ' x '
    fator -= 1

print(impressao + ' = ' + str(resultado))

#   SOLUÇÃO GUANABARA
print('{:=^60}'.format('SOLUÇÃO GUANABARA'))
n = int(input('Digite um nnúmero para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
