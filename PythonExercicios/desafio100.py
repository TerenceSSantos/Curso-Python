#   Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira
#   função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
#   os valores PARES sorteados pela função anterior.

from random import randint

def linha():
    print('=' * 60)


def somaPar(lst):
    linha()
    soma = 0
    for par in lst:
        if par % 2 == 0:
            soma += par
    print(f'Somando os valores pares de {lst}, temos {soma}')
    linha()


def sorteio():
    linha()
    lista = []
    for i in range(0, 5):
        lista.append(randint(0, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for c in lista:
        print(f'{c}', end=' ')
    print('PRONTO!')
    somaPar(lista)


sorteio()