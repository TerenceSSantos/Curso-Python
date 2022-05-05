#   Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#   Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep

def linha():
    print('=' * 60)


def maior(lista):
    linha()
    print(f'Analisando os valores passados...')
    for c in lista:
        sleep(0.2)
        print(f'{c}', end=' ')
    print(f'foram informados. {len(lista)} valores ao todo')
    print(f'O maior valor informado foi {max(lista)}')


linha()
num = []
for i in range(0, 5):
    while True:
        qt = randint(1,10)
        if qt > 1:
            for i in range(0, qt):
                num.append(randint(1, 10))
            maior(num)
            num.clear()
            break

def maiorGuanabara(*num):
    cont = maiorG = 0
    print('Analisando os valores passados... "')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maiorG = valor
        else:
            if valor > maiorG:
                maiorG = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maiorG}.')


#   VERSÃO GUANABARA
print('=' * 60)
print(f'{"VERSÃO GUANABARA":^60}')
print('=' * 60)
maiorGuanabara(2, 9, 4, 5, 7, 1)
maiorGuanabara(4, 7, 0)
maiorGuanabara(1, 2)
maiorGuanabara(6)
maiorGuanabara(0)