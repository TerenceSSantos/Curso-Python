#   Exeções

# r = 8 / 0 Abaixo vem o tratamento desta exceção
try:
    r = 8 / 0
except:
    print('Infelizmente tivemos um problema')
else:
    print(8 / 2)
finally:
    print('finally é sempre executado')

'''
MODOS DE EXCEPTIONS
except (ValueError, TypeError):
    print(tivemos um problema com os tipos de dados)
    
except Exception as erro:   criada variavel erro para exceção
    print(O erro encontrado foi {erro.__cause__})
'''