def leiaInt(msg):
    valor = 0
    while True:
        try:
            valor = int(msg)
            break
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar um valor Inteiro\033[m')
            value = 0
            break
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            msg = input('Digite um número inteiro: ')
        else:
            print('\033[31m ERRO! Digite um número inteiro válido.\033[m ')
            msg = input('Digite um número inteiro: ')
    return valor


def leiaFloat(msg):
    valor = 0
    while True:
        try:
            valor = float(msg)
            break
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar um valor Real\033[m')
            value = 0
            break
        except ValueError:
            print('\033[31mERRO! Digite um número Real válido.\033[m')
            msg = input('Digite um número Real: ')
        else:
            print('\033[31m ERRO! Digite um número Real válido.\033[m')
            msg = input('Digite um número Real: ')
    return valor


def mensagem(numInt, numReal):
    print(f'O número inteiro digitado foi {numInt} e o real foi {numReal}')