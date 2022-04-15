print('{:=^60}'.format(' COM LAÇO FOR '))
for c in range(1,10):
    print(c, end='-')
print('Fim!')

print('{:=^60}'.format(' COM LAÇO WHILE '))
c = 1
while c < 10:
    print(c, end='-')
    c += 1
print('Fim!' )

print('{:=^60}'.format(' OUTRO EXEMPLO WHILE '))
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es)'.format(par, impar))