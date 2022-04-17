# aula sobre tuplas
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)   # imprime a lista completa
print(lanche[2])    # imprime o item na posição 2
print(lanche[1:3])  # imprime da posição 1 até a posição 2, a última posição (3 no caso) é desconsiderada
print(lanche[2:])   # imprime da posição 2 até o final
print(lanche[:2])   # imprime da posição inicial até a 1. A posição 2 é desconsiderada
print(lanche[-2])   # a impressão parte do final. -2 é a Pizza
print(lanche[-3:])  # a impressão parte do final até
print(lanche[-4])   # no caso imprime a primeira posição dessa nossa lista.

print('=' * 60)
for comida in lanche:
    print(f'Eu vou comer {comida}')

print('=' * 60)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('=' * 60)
print(sorted(lanche))