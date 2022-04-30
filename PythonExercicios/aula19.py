#   Dicionários

dados = dict()
dados = {'nome':'Pedro', 'idade':25} # Outra forma é: dados = dict(nome='Pedro', idade=25)
print(dados['nome']) # Printará Pedro
print(dados['idade']) # Printará 25
print(dados)
dados['sexo'] = 'M' # Acrescenta o sexo a estrutura
print(dados)
del dados['idade'] # remove a idade da estrutura
print(dados)

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor': 'George Lucas'
}
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = list()
locadora.append(filme)
filme['titulo'] = 'Avengers'
filme['ano'] = 2012
filme['diretor'] = 'Joss Whedon'
locadora.append(filme)
print(locadora)
filme = {'titulo':'Matrix', 'ano':1999, 'diretor': 'Wachowski'}
locadora.append(filme)
print(locadora)

pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # O Gustavo tem 22 anos
print(pessoas.keys()) # dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) # dict_values(['Gustavo', 'M', 22])
print(pessoas.items()) # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
for k, v in pessoas.items():   # nome = Gustavo
    print(f'{k} = {v}')        # sexo = M
                               # idade = 22


brasil = list()
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(f'Sigla do estado 2: {brasil[1]["sigla"]}')

Estado = dict()
Brasil = list()
for c in range(0, 3):
    Estado['uf'] = str(input('Unidade Federativa: '))
    Estado['sigla'] = str(input('Sigla do Estado: '))
    Brasil.append(Estado.copy())
print(Brasil) # [{'uf': 'Minas Gerais', 'sigla': 'MG'}, {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(Estado.items())

for e in Brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
''' RESULTADO DO FOR ACIMA
O campo uf tem valor Minas Gerais.
O campo sigla tem valor MG.
O campo uf tem valor Rio de Janeiro.
O campo sigla tem valor RJ.
O campo uf tem valor São Paulo.
O campo sigla tem valor SP.'''