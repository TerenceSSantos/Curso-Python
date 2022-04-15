#   Crie um programa que simule o funcionamento de um caixa eletrônico.
#   No início pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
#   cédulas de cada valor serão entregues.
#   OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print('=' * 60)
print('{:^60}'.format('BANCO CURSO EM VIDEO'))
print('=' * 60)
valor = int(input('Que valor você quer sacar? R$ '))
print('-' * 60)
qt200 = qt100 = qt50 = qt20 = qt10 = qt1 = 0
while valor > 0:
    if valor >= 200:
        qt200 = valor // 200
        valor -= qt200 * 200
        print(f'Total de {qt200} cédulas de R$ 200,00')
    elif valor < 200:
        if valor >= 100:
            qt100 = valor // 100
            valor -= qt100 * 100
            print(f'Total de {qt100} cédulas de R$ 100,00')
        elif valor < 100:
            if valor >= 50:
                qt50 = valor // 50
                valor -= qt50 * 50
                print(f'Total de {qt50} cédulas de R$ 50,00')
            elif valor < 50:
                if valor >= 20:
                    qt20 = valor // 20
                    valor -= qt20 * 20
                    print(f'Total de {qt20} cédulas de R$ 20,00')
                elif valor < 20:
                    if valor >= 10:
                        qt10 = valor // 10
                        valor -= qt10 * 10
                        print(f'Total de {qt10} cédulas de R$ 10,00')
                    elif valor < 10:
                        if valor >= 1:
                            qt1 = valor // 1
                            valor -= qt1 * 1
                            print(f'Total de {qt1} cédulas de R$ 1,00')
print('=' * 60)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')