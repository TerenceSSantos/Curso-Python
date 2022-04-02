nome = str(input("Digite um nome: ")).strip()
aux = nome.split()
print('Primeiro nome:', aux[0])
print('Último nome:', aux[(len(aux) - 1)])