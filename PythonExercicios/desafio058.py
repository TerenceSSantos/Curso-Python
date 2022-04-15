#    Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
#    quantos palpites foram necessários para vencer.

from random import choice

n = int(input('Qual o número que estou pensando de 0 à 10? '))

contador = 1
resultado = choice([0,1,2,3,4,5,6,7,8,9,10])
while n != resultado:
    print('-'*60)
    print('Errou!. Terá que tentar novamente')
    if resultado > n:
        print('O número que pensei é maior')
        print('-' * 60)
    elif resultado < n:
        print('O número que pensei é menor')
        print('-' * 60)
    n = int(input('Digite o número: '))
    print('-' * 60)
    contador += 1
print('Parabéns, você acertou! Precisou de {} chances para acertar'.format(contador))

# Método alternativo com randint
from random import randint

print('{:=^60}'.format('COM RANDINT'))
contador = 1
computador = randint(0,10)
jogador = int(input('Qual o número que estou pensando de 0 à 10? '))
while jogador != computador:
    print('-' * 60)
    print('Errou!. Terá que tentar novamente')
    if computador > jogador:
        print('O número que pensei é maior')
        print('-' * 60)
    elif computador < jogador:
        print('O número que pensei é menor')
        print('-' * 60)
    jogador = int(input('Digite o número: '))
    print('-' * 60)
    contador += 1
print('Parabéns, você acertou. Precisou de {} chances para acertar.'.format(contador))
