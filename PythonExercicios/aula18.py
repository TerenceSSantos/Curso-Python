#   Variáveis Compostas (listas) parte 2

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] # Uma lista dentro da outra
for p in pessoas:
    print('Esse é o for de pessoas ',p)
    print(f'Esse mostra o nome: {p[0]} \nE esse a idade: {p[1]}')
print('-' * 60)
print(pessoas[0][0])    # printará Pedro
print(pessoas[1][1])    # printará 19
print(pessoas[2][0])    # printará João
print(pessoas[1])       # printará ['Maria', 19]
print('=' * 60)
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:]) # Se não colocar o [:], que significa todos os ítens, ele criará um link, duplicando então
print(f'Printando galera: {galera}') # o registro [Maria, 22]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(f'Printando galera novamente: {galera}')