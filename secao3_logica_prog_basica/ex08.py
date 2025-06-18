"""
Exercício com while
"""
nome = 'Maria Helena'

letra = 0
novo_nome = ''

while letra < len(nome):
    letra_indice = nome[letra]
    novo_nome += f'*{letra_indice}'
    letra += 1

novo_nome += '*'
print(novo_nome)
