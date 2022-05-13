from time import sleep

def inserir():
    print('-' * 60)
    print(f'{"NOVO CADASTRO":^60}')
    print('-' * 60)
    nome = input('Nome: ')
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except:
            print('\033[31m Informe uma idade válida! \033[m')
    f = open('BD.txt', 'a')
    f.write(f'{nome:<40}{idade:>3} anos \n')
    f.close()
    print(f'\033[36m O registro de {nome} foi adicionado com sucesso! \033[m')
    sleep(2)