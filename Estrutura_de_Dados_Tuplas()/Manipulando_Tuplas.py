coordenadas = ('10.0', '20.5', '15.0')
print(f'Tupla de coordenadas: {coordenadas}')
print(f'O tipo da tupla:{type(coordenadas)}')

#acessando um item pelo índice
print(f'A tupla tem {len(coordenadas)} elementos')
print(f'Coordenada x : {coordenadas[0]}')
print(f'Coordenada y : {coordenadas[1]}')
print(f'Coordenada z : {coordenadas[-1]}')

#tentar modificar uma tupla resulta em erro são imutáveis
#coordenadas[0]= 13
#print(f'Coordenada x : {coordenadas[0]}')

#Tuplas são úteis para dados que não podem ser alterados tipo datas, coordenadas.
dias_da_semana = ('segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira','sabado', 'domingo')
print(dias_da_semana)
print(f'O primeiro dia da semana : {dias_da_semana[0]}')

dias_da_semana = ('segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sabado', 'domingo', ' Domingofake')

# Procurando o primeiro dia que começa com 'd'
encontrado = []
cont = 0
for dia in dias_da_semana:
    if dia.lower().strip().startswith('d'):
        encontrado.append(dia)
        cont += 1
        #break  # Para no primeiro que encontrar
print(f'Aqui é uma lista{encontrado}')
nova_tupla_diaD = tuple(encontrado)
print(f'Aqui tranformei em tupla {nova_tupla_diaD}')

dias_da_semana = ('segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sabado', 'domingo', 'Domingofake')

# Busca o primeiro item que começa com 'd' (convertendo para minúsculas para evitar problemas com maiúsculas/minúsculas)
dias_com_d = next((dia for dia in dias_da_semana if dia.lower().strip().startswith('d')), None)

print(f'Oprimeiro dia encontrado com a  letra D é: {dias_com_d}')

print(f'Os dias encontrados com a letra D é: {encontrado} tem {cont} elementos')

