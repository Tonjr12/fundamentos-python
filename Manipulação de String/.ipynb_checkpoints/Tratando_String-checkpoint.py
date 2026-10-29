#definir uma variavél
frase = '   Aprender Python é muito Divertido!   '
print(f'A frase sem sem tratamento: "{frase}"')

#concatenação
nome = 'Washington'
saudacao = 'Olá, ' + nome + ' Bom Dia!'
print(saudacao)

#tamanho da string
print(f'tamanho da frase : {len(frase)}')#contando o número de letras e de espaços

#maiúsculas e minúsculas
print(f'Maiuscula: {frase.upper()}')
print(f'Minuscula: {frase.lower()}')

#remover espaços em branco do início e fim
frase_sem_espaco = frase.strip()
print(f'A frase sem espaços: "{frase_sem_espaco}"')

#substituir texto
print(f'Substituido "Divertido" por "Legal": {frase_sem_espaco.replace("Divertido", "Legal")} ')

print(f'{frase_sem_espaco}')#agora trabalhando com uma nova variável

#fatiamento (slicing) - acessando partes de uma ‘string’
#indice em python sempre começa com zero
print(f'O primeiro caractere: {frase_sem_espaco[0]}')
#O indice em Python sempre começa com zero e para um antes (ex:15 -1)
print(f'A palavra "Python": {frase_sem_espaco[9:15]}')#do 9 ao 14







