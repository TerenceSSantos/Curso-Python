#   Aprimore o desafio anterior, mostrando no final:
#   A) A soma de todos os valores pares digitados.
#   B) A soma dos valores da terceira coluna.
#   C) O maior valor da segunda linha.

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
par = 0
terceira = 0
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end='')
        if matriz[i][j] % 2 == 0:
            par += matriz[i][j]
        if j == 2:
            terceira += matriz[i][j]
    print()
print('-' * 60)
print(f'A soma dos valores pares é de {par}')
print(f'A soma dos valores da teceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

#   MÉTODO DO GUANABARA
print('=' * 60)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é: {mai}')