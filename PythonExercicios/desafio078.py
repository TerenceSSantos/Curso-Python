#   Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#   No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print('=' * 60)
lista = [] # lista = list()
posmaior = []
posmenor = []
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if maior <= lista[i]:
            maior = lista[i]
        if menor >= lista[i]:
            menor = lista[i]
for i in range(0, len(lista)):
    if lista[i] == maior:
        posmaior.append(i)
for i in range(0, len(lista)):
    if lista[i] == menor:
        posmenor.append(i)
print('-' * 60)
print(f'Você digitou os valores {lista}')
print('-' * 60)
print(f'O maior valor digitado foi {maior} na posição {posmaior}')
print('-' * 60)
print(f'O menor valor digitado foi {menor} na posição {posmenor}')
print('-' * 60)
print('USANDO MAX. ', max(lista))
print('USANDO MIN ', min(lista))

