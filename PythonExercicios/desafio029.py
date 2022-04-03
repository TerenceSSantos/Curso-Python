velocidade = int(input('Por favor informe a velocidade do carro: '))
if velocidade > 80:
    print('Você excedeu o limite de velocidade.')
    print('Deverá pagar uma multa de R$ {:.2f}'.format((velocidade - 80) * 7))
else:
    print('Parabéns por se manter dentro do limite de velocidade')