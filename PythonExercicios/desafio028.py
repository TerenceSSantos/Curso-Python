
from random import choice

n = int(input('Qual o número que estou pensando de 0 à 5? '))
resultado = choice([0,1,2,3,4,5])
if n == resultado:
    print('Parabéns, você acertou!')
else:
    print('Você errou, pensei no número', resultado)

# Método alternativo com randint
from random import randint

computador = randint(0,5)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))


