#   Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
#   retangular(largura e comprimento) e mostre a área do terreno.

def area(a, b):
    print(f'A área de um terreno {a} x {b} é de {a * b}m²')


print('=' * 60)
print(f'{"Controle de Terrenos":^60}')
print('=' * 60)
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
area(larg, compr)