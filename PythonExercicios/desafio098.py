#   Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros: início, fim e passo e
#   realize a contagem. Seu programa tem que realizar 3 contagens através da função criada:
#   A) de 1 até 10, de 1 em 1
#   B) de 10 até 0, de 2 em 2
#   C) uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passo):
    if (inicio == 1 and fim == 10 and passo == 1) or (inicio == 10 and fim == 0 and passo == 2):
        print('=' * 60)
        print('Contagem de 1 até 10 de 1 em 1')
        for i in range(1, 11):
            sleep(0.3)
            print(f'{i} ', end='')
        print('FIM!')
        print('=' * 60)
        print('Contagem de 10 até 0 de 2 em 2')
        for i in range(10, -1, -2):
            sleep(0.3)
            print(f'{i} ', end='')
        print('FIM!')
    else:
        if passo == 0:
            passo = 1
        elif passo < 0:
            passo = passo * -1
        if inicio < fim:
            print('=' * 60)
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            for i in range(inicio, fim + 1, passo):
                sleep(0.3)
                print(f'{i} ', end='')
            print('FIM!')
        elif inicio > fim:
            print('=' * 60)
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            for i in range(inicio, fim - 1, -passo):
                sleep(0.3)
                print(f'{i} ', end='')
            print('FIM!')


contador(1, 10, 1)
print('=' * 60)
print('Agora é a sua vez de personalizar a contagem!')
while True:
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if (inicio == 1 and fim == 10 and passo == 1) or (inicio == 10 and fim == 0 and passo == 2):
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}, já foi exibido, faça outra escolha')
    #elif inicio == 10 and fim == 0 and passo == 2:
     #   print(f'Contagem de {inicio} até {fim} de {passo} em {passo}, já foi exibido, faça outra escolha')
    else:
        break
contador(inicio, fim, passo)