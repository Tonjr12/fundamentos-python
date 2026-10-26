dias_da_semana = ('segunda-feira', 'terça-feira', 'quarta-feira','quinta-feira',
                  'sexta-feira','sexta-feiraFake','sabado', 'domingo', 'domingofake')
dias_com_s_ou_d_ou_q = []


cont = 0



for indice, dia in enumerate(dias_da_semana):
    if dia.lower().strip().startswith(('s','d','q')):
        dias_com_s_ou_d_ou_q.append(dia)
        cont += 1
        posicao_de_s = indice + 1
        print(f"O item '{dia}' foi encontrado na posição {posicao_de_s}ª da tupla.")

print(dias_com_s_ou_d_ou_q)
print(f"\nLista com todos os encontrados: {dias_com_s_ou_d_ou_q}")
print(f"Total de elementos encontrados: {cont}")
tupla_modificada_sem_tercafeira = tuple(dias_com_s_ou_d_ou_q)
print(tupla_modificada_sem_tercafeira)

# Busca o primeiro item que começa com 't' (convertendo para minúsculas para evitar problemas com maiúsculas/minúsculas)

indice_encontrado,dias_com_t = next(
    ((indice,dia) for indice,dia in enumerate (dias_da_semana) if dia.lower().strip().startswith('t')),(None , None)
)
print(f'O primeiro dia encontrado com a letra T é: {dias_com_t}')
print(f'A localização (índice) dele na tupla é: {indice_encontrado} (ou seja, a {indice_encontrado + 1}ª posição)')