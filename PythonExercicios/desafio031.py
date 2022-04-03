km = float(input('Quandos quilometros terá sua viagem? '))
print('='*50)
if km <= 200:
    print('O valor da sua viagem é de: R$ {:.2f}'.format(km * 0.5))
else:
    print('O valor da sua viagem é de: R$ {:.2f}'.format(km * 0.45))


# Modo simplificado ou inline
print('='*50)
print('O valor da sua viagem é de: R$ {:.2f}'.format(km * 0.5)) if km <= 200 else print('O valor da sua viagem é de: R$ {:.2f}'.format(km * 0.45))
