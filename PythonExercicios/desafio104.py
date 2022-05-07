#   Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
#   só que fazendo a validação para aceitar apenas um valor numérico.
#   Exemplo: n = leiaInt('Digite um número: ')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31m ERRO! Digite um número inteiro válido.\033[m ')
        if ok:
            break
    return valor


#   PROGRAMA PRINCIPAL
print('=' * 60)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')