#   Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
#   de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from cadastrar import inserir
from leitura import listar
from time import sleep

while True:
    print('=' * 60)
    print(f'{"MENU PRINCIPAL":^60}')
    print('=' * 60)
    print('\033[33m 1 -\033[m \033[34m Ver pessoas cadastradas \033[m')
    print('\033[33m 2 -\033[m \033[34m Cadastradar nova Pessoa \033[m')
    print('\033[33m 3 -\033[m \033[34m Sair do Sistema \033[m')
    print('=' * 60)
    opcao = input('\033[33m Sua opção: \033[m')
    if opcao == '2':
        inserir()
    elif opcao == '1':
        listar()
    elif opcao == '3':
        print('-' * 60)
        print(f'\033[36m{"SAINDO DO SISTEMA, ATÉ A PRÓXIMA...":^60} \033[m')
        print('-' * 60)
        sleep(2)
        break
    else:
        print('\033[31m Opção inválida! Digite uma opção válida \033[m')
        sleep(1.5)
