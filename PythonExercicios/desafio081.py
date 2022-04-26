#   Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
#   A) Quantos números foram digitados.
#   B) A lista de valores ordenada de forma descrescente
#   C) Se o valor 5 foi digitado e está ou não na lista.

print('=' * 60)
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = (input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('-' * 60)
print(f'Você digitou {len(lista)} elementos')
print('-' * 60)
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
print('-' * 60)
if lista.__contains__(5): # if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista')