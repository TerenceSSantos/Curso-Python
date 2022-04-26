#   Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#   já na posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.

print('=' * 60)
num = []
valor = 0
for c in range(0, 5):
    tamanho = len(num)
    valor = int(input('Digite um valor: '))
    if len(num) == 0:
        num.append(valor)
        print('Adicionado ao final da lista!')
    elif valor < num[0]:
        num.insert(0, valor)
        print('Valor adicionado na posição 0')
    elif valor > num[tamanho - 1]:
        num.append(valor)
        print('Adicionado ao final da lista!')
    elif valor in num:
        num.insert(num.index(valor), valor)
        print(f'Valor {valor} adicionado na posição {num.index(valor)}')
    else:
        for i in range(0, tamanho-1):
            if valor > num[i] and valor < num[i+1]:
                num.insert(i+1, valor)
                print(f'Valor {valor} adicionado na posição {num.index(valor)}')
print('-' * 60)
print('Os números digitados foram:', num)

