dias_da_semana = ('segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sabado', 'domingo', ' Domingofake')

# 1. Criamos uma lista vazia para filtrar os itens
lista_com_d = []

for dia in dias_da_semana:
    if dia.lower().strip().startswith('d'):
        lista_com_d.append(dia)

# 2. Convertemos a lista filtrada de volta para uma nova tupla
tupla_somente_d = tuple(lista_com_d)

print(f"Lista intermediária: {lista_com_d}")
print(f"Tupla final modificada: {tupla_somente_d}")
print(f"O tipo agora é: {type(tupla_somente_d)}")