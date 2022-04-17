#   Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
#   Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import  randint
'''
maior = menor = 0
num1 = num2 = num3 = num4 = num5 = 0
for i in range(0, 5):
    if i == 0:
        num1 = randint(0, 10)
    elif i ==1:
        num2 = randint(0, 10)
    elif i == 2:
        num3 = randint(0, 10)
    elif i == 3:
        num4 = randint(0, 10)
    elif i == 4:
        num5 = randint(0, 10)
'''

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
'''
for i in range(0, len(tupla)):
    if i == 0:
        maior = menor = tupla[i]
    elif maior < tupla[i]:
        maior = tupla[i]
    elif menor> tupla[i]:
        menor = tupla[i]
'''

print('-' * 60)
print(f'Os valores sorteados foram: {tupla}')
print('-' * 60)
print(f'O maior valor sorteado foi: {max(tupla)}')  # {maior}
print('-' * 60)
print(f'O menor valor sorteado foi: {min(tupla)}')  # {menor}
print('-' * 60)