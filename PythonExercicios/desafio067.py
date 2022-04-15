# Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

n = 0
while True:
    print('-' * 60)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 60)
    if n < 0:
        break
    else:
        for i in range(1, 11):
            print(f'{n} X {i} = {n * i}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')