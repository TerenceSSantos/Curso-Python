sal = float(input('Por favor informe o valor do salário R$ '))
if sal > 1250:
    print('O valor do novo salário será R$ {:.2f}'.format(sal * 1.1))
else:
    print('O valor do novo salário será R$ {:.2f}'.format(sal * 1.15))