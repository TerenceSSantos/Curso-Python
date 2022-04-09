# solicitar um número e fazer sua tabuada

print('\n{:=^120}'.format(' TABUADA '))
n = int(input('Gostaria de fazer a tabuada de qual número? \n'))
print('-'*40)
for i in range(1, 10):
   print('{} X {} = {:2}'.format(n, i, i * n))
