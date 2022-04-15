#   Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar
#   se o usuário que ou não continuar. No final mostre:
#   A)  quantas pessoas tem mais de 18 anos.
#   B)  Quantos homens foram cadastrados.
#   C)  Quantas mulheres tem menos de 20 anos.

print('{:=^60}'.format('INÍCIO DO PROGRAMA'))
continuar = 'S'
idade = maior = menor = homens = 0
sexo = 'i'
while continuar == 'S':
    print('-' * 40)
    print('{:^40}'.format('CADASTRE UMA PESSOA'))
    print('-' * 40)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo not in 'MF':
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    print('-' * 40)
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar not in 'SN':
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        menor += 1
print('{:=^40}'.format('FIM DO PROGRAMA'))
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homem(s) cadastrado(s)')
print(f'E temos {menor} mulher(es) com menos de 20 anos')