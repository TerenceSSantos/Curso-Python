print('\n{:=^60}'.format(' LOJA '))
preco = float(input('Informe o valor do produto: '))
print('==='*20)
print('Selecione a forma de pagamento')
print('==='*20)
print('1 - DINHEIRO')
print('2 - CHEQUE')
print('3 - CARTÃO')
print('==='*20)
pag = int(input('Forma de pagamento: '))
print('==='*20)
if pag > 3:
   print('Opção inválida!!')
if pag == 3:
   print('Parcelado ou à vista?')
   print('V = à vista')
   print('P = parcelado')
   tp_parc = input('Método: ')
   if tp_parc.upper() == 'P':
      print('==='*20)
      qt_vezes = int(input('Informe quantidade de parcelas: '))
if pag == 1 or pag == 2:
   print('Valor a pagar R$ {:.2f}'.format(preco - (preco * 0.1)))
elif pag == 3:
   if tp_parc.upper() == 'V':
      print('Valor à pagar R$ {:.2f}'.format(preco - (preco * 0.05)))
   elif qt_vezes == 2:
      print('Valor à pagar R$ {:.2f}'.format(preco))
   elif qt_vezes > 2:
      print('Valor com juros R$ {:.2f}'.format(preco + (preco * 0.2)))
      print('Parcelas no valor de R$ {:.2f}'.format((preco + (preco * 0.2)) / qt_vezes))
