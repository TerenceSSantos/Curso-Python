#   Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999.
#   No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).

print('='*60)
contador = valor = soma = sair = 0
while sair != 999:
    print('Digite um nº inteiro ou')
    print('Digite 999 para encerrar')
    valor = int(input('Nº: '))
    if valor == 999:
        sair = 999
    else:
        contador += 1
        soma += valor
print('-'*60)
print('Foram informados {} números'.format(contador))
print('A soma de todos eles deu {}'.format(soma))