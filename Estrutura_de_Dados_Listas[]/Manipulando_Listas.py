#criado uma lista
frutas = ['maçã','banana','laranja','abacaxi']
print(f'A lista de frutas: {frutas}')

#mostrando a classe
print(f'Mostrando o tipo: {type(frutas)}')

#acessando o intem pelo índice
print(f'A primeira fruta: {frutas[0]}')
print(f'A ultima fruta: {frutas[-1]}')

#adicionando um item ao final da lista usando 'append'
frutas.append('uva')
print(f'A lista de frutas com a "uva" adicionda: {frutas}')

#removendo um item usando 'remove'
frutas.remove('laranja')
print(f'A lista com a "laranja" removida: {frutas}')

#modificando um item
frutas[0] = 'morango'
print(f'Lista após modificar o primeiro item: {frutas}')

#verificando o tamanho da lista usando 'len'
print(f'A lista tem, {len(frutas)} frutas ')

#deletando um item da lista
del frutas[0]
print(f'A lista tem, {len(frutas)} frutas ')
print(frutas)

#deletando a lista toda
del frutas
# Já não pode ser acessada print(frutas)
