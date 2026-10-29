aluno = {
    "Nome": "Ton",
    "Idade": 25,
    "Curso": "Curso de Python",
    "aluno_ativo":True
}
for chave,valor in aluno.items():
    print(f'{chave} : {valor}')

for indice,(chave,valor) in enumerate(aluno.items()):
    print(f"{indice +1}: {chave} = {valor}")

#pythonico
ordem ,( chave , valor) = next (
    (enumerate(aluno.items()))
)
print(f"Ordem: {ordem +1}")
print(f"Chave: {chave}")
print(f"Valor: {valor}")

