#   Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
#   A)  Quantas vezes apareceu o valor 9
#   B)  Em que posição foi digitado o 1º valor 3
#   C)  Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print('-' * 60)
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:  # tupla.__contains__(3):
    print(f'O varlor 3 apareceu na posição {num.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print(end='\n')
print('-' * 60)
