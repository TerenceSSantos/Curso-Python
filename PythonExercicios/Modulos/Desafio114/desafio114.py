#   Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import requests

url = 'http://pudim.com.br'
try:
    if requests.get(url).status_code == 200:
        print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
except:
    print('\033[31mNão foi possível acessar o site Pudim!\033[m')