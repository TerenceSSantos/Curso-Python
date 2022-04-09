#  Fazer uma contagem regressiva de 10 à 0 com uma pausa de 1 segundo entre a contagem

from time import sleep


print('\n{:=^120}'.format(' CONTAGEM REGRESSIVA '))
sleep(2)
print('ATENÇÃO PARA A CONTAGEM')
sleep(1)
for i in range(10, -1, -1):
   print('\033[1;32;40m {:2} \033[m'.format(i))
   sleep(1)
print('BUM, BUM, BUM, POW')