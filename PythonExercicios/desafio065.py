# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar digitando valores.

print('='*60)
continuar = 'S'
cont = maior = menor = soma = 0
repete_mensasgem = 'N'
while continuar == 'S':
    repete_mensasgem = 'N'
    valor = int(input('Digite um nº inteiro: '))
    cont += 1
    soma += valor
    if cont == 1:
        maior = menor = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    print('-'*60)
    while repete_mensasgem != 'S':
        continuar = str(input('Deseja continuar? [S ou N]')).upper()
        if continuar == 'N':
            repete_mensasgem = 'S'
        else:
            repete_mensasgem = continuar
    print('-'*60)
media = soma / cont
print('A média dos valores digitados foi {:.2}'.format(media))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))
print('Foram digitados {} números'.format(cont))