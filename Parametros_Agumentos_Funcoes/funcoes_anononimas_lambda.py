dobro = lambda x: x * 2
print(dobro(7))

'''A grande vantagem de usar expressões lambda em Python é a simplicidade e concisão para criar funções pequenas, temporárias e sem nome (anônimas).

Normalmente, quando você precisa de uma função, define com def. Mas às vezes a função é muito simples e usada apenas uma vez, dentro de outra operação (como um map, filter ou sorted). Nesses casos, a lambda evita código extra e deixa o fluxo mais direto.

Você pode combinar uma expressão lambda com a função map() para aplicar uma operação a cada elemento da lista, por exemplo.'''
#lista de números
numeros = [1, 2, 3, 4, 5]
print(f'A lista original: {numeros}')

# Primeiro calculamos os quadrados com map + lambda
quadrados = list(map(lambda x: x**2, numeros))
print(f'A lista ao quadrado{quadrados}')
# Agora filtramos apenas os pares com filter + lambda
quadrados_pares = list(filter(lambda x: x%2 == 0, quadrados))
print(f'A lista ao quadrado{quadrados_pares}')


