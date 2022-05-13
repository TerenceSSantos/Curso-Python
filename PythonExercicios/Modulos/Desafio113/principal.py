#   Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
#   número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from lernumeros import leiaInt, leiaFloat, mensagem

try:
    inteiro = leiaInt(input('Digite um número inteiro: '))
except KeyboardInterrupt:
    inteiro = 0
    print(f'\033[31mUsuário preferiu não digitar um valor Inteiro\033[m')
try:
    real = leiaFloat(input('Digite um número Real: '))
except KeyboardInterrupt:
    real = 0
    print(f'\033[31mUsuário preferiu não digitar um valor Real\033[m')
mensagem(inteiro, real)
