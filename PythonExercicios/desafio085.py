#   Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que
#   mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

print('=' * 60)
numeros = list()    # forma alternativa de declaração: numeros = [[], []]
par = list()
impar = list()
for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
par.sort()
numeros.append(par[:])
impar.sort()
numeros.append(impar[:])
print('-' * 60)
print(f'Os valores PARES digitados foram: {numeros[0]}')
print(f'Os valores ÍMPARES digitados foram: {numeros[1]}')
print(f'A lista de números {numeros}')
print('-' * 60)

#   MÉTODO DO GUANABARA
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Todos os valores: {num}')
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')