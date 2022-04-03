n1 = int(input('Por favor informe um número: '))
n2 = int(input('Por favor informe outro número: '))
n3 = int(input('Por favor informe outro número: '))
if n1 > n2 and n1 > n3:
    print(n1, 'é o maior número')
elif (n2 > n1) and (n2 > n3):
    print(n2, 'é o maior número')
elif n3 > n1 and n3 > n2:
    print(n3, 'é o maior número')

if n1 < n2 and n1 < n3:
    print(n1, 'é o menor número')
elif n2 < n1 and n2 < n3:
    print(n2, 'é o menor número')
elif n3 < n1 and n3 < n2:
    print(n3, 'é o menor número')