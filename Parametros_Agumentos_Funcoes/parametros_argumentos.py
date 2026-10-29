def ton_apresentacao (nome,idade):
    print(f'Nome: {nome} tem idade: {idade} anos')

ton_apresentacao('Isabel', 18)

# Parâmetros com valores padrão (default)
def dsa_saudacao_completa(nome, saudacao = "Olá"):
    print(f"{saudacao}, {nome}!")
dsa_saudacao_completa('Ton')

dsa_saudacao_completa(1,2)

dsa_saudacao_completa("ton","bom dia")