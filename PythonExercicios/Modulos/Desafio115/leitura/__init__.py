from time import sleep

def listar():
    print('-' * 60)
    print(f'{"PESSOAS CADASTRADAS":^60}')
    print('-' * 60)
    f = open('BD.txt', 'r')
    print(f.read())
    sleep(1.5)
    f.close()