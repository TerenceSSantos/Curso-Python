from random import shuffle

aluno1 = input('Digite um nome de aluno: ')
aluno2 = input('Digite um nome de aluno: ')
aluno3 = input('Digite um nome de aluno: ')
aluno4 = input('Digite um nome de aluno: ')
nomes = [aluno1, aluno2, aluno3, aluno4]
shuffle(nomes)
print('Nomes {}'.format(nomes))