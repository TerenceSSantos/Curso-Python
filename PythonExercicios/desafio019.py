import random

aluno1 = input('Digite um nome de aluno: ')
aluno2 = input('Digite um nome de aluno: ')
aluno3 = input('Digite um nome de aluno: ')
aluno4 = input('Digite um nome de aluno: ')
print('O aluno escolhido foi {}'.format( random.choice([aluno1, aluno2, aluno3, aluno4])))