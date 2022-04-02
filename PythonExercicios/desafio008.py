n = float(input('Digite um valor em metros: '))
cm = n * 100
mm = n * 1000
km = n / 1000
print('...'*30)
print('{} metros são:\n{} centímetros \n{} milímetros, \n{} quilometros'.format(n, cm , mm, km))