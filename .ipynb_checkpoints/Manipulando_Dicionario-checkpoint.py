#criando um dicionario com informações de um aluno
aluno = {
    "Nome": "Ton",
    "Idade": 25,
    "Curso": "Curso de Python",
    "aluno_ativo":True
}
print(f'Dicionário: {aluno}')
print(f'Aluno: {aluno["Nome"]}')
print(f'curso: {aluno.get("Curso")}')#get maneira segura de acessar a chave.

#adicionando um novo par chave-valor
aluno['cidade'] = 'São Paulo'
print(f'Dicionario atual:\n{aluno}\nidade do aluno: \n{aluno.get("Idade") } anos')

#modificando idade
aluno['Idade'] = 23
print(f'Dicionario atual:\n{aluno}')

#Removendo um item por chave-valor
del aluno ["aluno_ativo"]
print(f'Dicionario atual com aluno ativo removido:\n{aluno}')