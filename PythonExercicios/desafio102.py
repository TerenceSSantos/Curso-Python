#   Crie um programa que tenha uma função fatorial() que receba 2 parâmetros: o primeiro que indique o número
#   a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
#   na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    => Função que calcula o fatorial de um número
    :param n: número do qual será calculado o fatorial
    :param show: (opcional). Mostrar ou não a conta
    :return: retornará o resultado do fatorial
    """
    if n <= 0:
        return f'Não é possível calcular o fatorial de {n}'
    elif n == 1:
        if  show == True:
            return ('1! = 1')
        else:
            return 1
    else:
        fat = str(n) + '!='
        total = 1
        for i in range(n, 0, -1):
            if i != 1:
                fat = fat + str(i) + ' x '
                total *= i
            else:
                fat = fat + str(i) + ' = ' + str(total)
        if show == True:
            return fat
        else:
            return total


#   PROGRAMA PRINCIPAL
print('=' * 60)
print(fatorial(5, True))
print('=' * 60)
help(fatorial)