#   Parte 1 da aula sobre funções.

def mostralinha():
    print('-' * 60)


mostralinha()
print(f'{"Sistema de Alunos":^60}')
mostralinha()
mostralinha()
print(f'{"Cadastro de Funcionários":^60}')
mostralinha()
mostralinha()
print(f'{" Erro do Sistema":^60}')
mostralinha()
print()
print('*' * 60)
print()


def mostralinha2(frase):
    print('-' * 60)
    print(f'{frase:^60}')
    print('-' * 60)


mostralinha2('SISTEMA DE ALUNOS')
mostralinha2('CADASTRO DE FUNCIONÁRIOS')
mostralinha2('ERRO DO SISTEMA')

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4,7, 6, 2)