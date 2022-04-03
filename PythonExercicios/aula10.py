nome = str(input('Qual é o seu nome? '))
if nome == 'Terence':
    print('Que nome lindo você tem.')
else:
    print('Seu nome é tão normal.')
print('Bom dia', nome)

n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1 + n2) / 2
print('A sua média  foi {:.1f}'.format(media))
if media >= 6:
    print('Sua média está boa. PARABENS!')
else:
    print('Sua média está ruim. ESTUDE MAIS')