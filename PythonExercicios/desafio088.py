#   Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
#   serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

print('=' * 60)
print('{:^60}'.format('JOGA NA MEGA SENA'))
print('=' * 60)
jogos = list()
volante = list()
qt_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:~^60}'.format(' SORTEANDO ' + str(qt_jogos) + ' JOGOS '))
for i in range(0, qt_jogos):
    for j in range(0, 6):
        volante.append(randint(1, 60))
    jogos.append(volante[:])
    volante.clear()
    print(f'Jogo {i + 1}: {jogos[i]}')
print('{:~^60}'.format(' < BOA SORTE! > '))

# VERSÃO GUANABARA
from time import sleep

lista = list()
jogos = list()
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)