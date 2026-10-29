# Cria um dicionário com números e seus quadrados
quadrados_dict = {x: x ** 2 for x in range(6)}

print(quadrados_dict)
for key, value in enumerate(quadrados_dict.items()):
    print(f'{key}: {value}')

#conjunto de valores (sem valores repetidos)
quadrados_set = {x ** 2 for x in {1,1, 2,2, 3,3, 4}}
ordem = sorted(quadrados_set)
print(f'\n set ficom em ordem {ordem}')

# Generator expression (não é tupla ainda)
gen = (x ** 2 for x in range(6))
print(gen)

# Convertendo em tupla
quadrados_tuple = tuple(x ** 2 for x in range(6))
print(f'\nvirou tupla:{quadrados_tuple}' )# Está entre parenteses

quadrados_lista = list(quadrados_tuple)
print(f'virou lista: {quadrados_lista}')# está entre conchetes

quadrados_dicionario = {x : x ** 2 for x in range(6)}
print(f'virou dicionario: {quadrados_dicionario}')