#   Crie um programa que leia dois valores e mostre um menu na tela:
#   [ 1 ] somar
#   [ 2 ] multiplicar


menu = 1
while menu != 0:
    print('-' * 60)
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    print('{:=^60}'.format('ESCOLHA A OPÇÃO'))
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')
    print('-'*60)
    menu = int(input('Escolha a opção correta: '))
    if menu != 1 and menu != 2 and menu != 3 and menu != 4  and menu != 5:
        while str(menu) not in '1,2,3,4,5':
            menu = int(input('Inválido. Digite a operação: '))
    else:
        print('-' * 60)
        if menu == 5:
            print('Adeus, volte sempre!')
            menu = 0
        elif menu == 1:
            print('A soma de {} + {} resulta em: {}'.format(n1, n2, n1 + n2))
        elif menu == 2:
            print('A multiplicação de {} X {} resulta em: {}'.format(n1, n2, n1 * n2))
        elif menu == 3:
            if n1 > n2:
                print('O 1º nº {} é maior que o 2º nº {}'. format(n1, n2))
            elif n2 > n1:
                print('O 2º nº {} é maior que o 1º nº {}'.format(n2, n1))
            else:
                print('Os 2 tem o mesmo valor!')
        elif menu == 4:
            menu = 1