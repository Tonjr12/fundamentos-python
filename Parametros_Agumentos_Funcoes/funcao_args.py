def ton_soma_numeros(*args):
    total = 0
    for n in args:
        total += n
    return total
print(ton_soma_numeros(1,2,3,4,5,6,7,8,9))
print(ton_soma_numeros(1,2,3))
print(ton_soma_numeros(1,2))

# Argumentos de tamanho variável (**kwargs)
def ton_info_pessoas(**kwargs):
    """Exibe informações passadas como pares chave-valor."""
    for chave, valor in kwargs.items():
        print(f'-{chave}: {valor}')
ton_info_pessoas(Nome = 'Ton',
                 Profissao = 'Arquiteto de Dados',
                 Idade = 18)
# Chamando a função
ton_info_pessoas(nome = "Bob" , profissao = "Cientista de Dados")
ton_info_pessoas(nome = "Ton", profissao = "Engenheiro de dados")


