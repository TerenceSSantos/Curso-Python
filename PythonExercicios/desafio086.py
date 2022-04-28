#   Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#   No final mostre na tela com a formatação correta

print('=' * 60)
matriz = list()
linha1 = list()
linha2 = list()
linha3 = list()
for i in range(0, 3):
    linha1.append(int(input(f'Digite um valor para [0, {i}]: ')))
for i in range(0, 3):
    linha2.append(int(input(f'Digite um valor para [1, {i}]: ')))
for i in range(0, 3):
    linha3.append(int(input(f'Digite um valor para [2, {i}]: ')))
matriz.append(linha1[:])
matriz.append(linha2[:])
matriz.append(linha3[:])
print('-' * 60)
print(f'Esta é lista preenchida: {matriz}')
print('A seguir a matriz')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()

#   MÉTODO DO GUANABARA
print('=' * 60)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()