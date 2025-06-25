"""
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índice e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    del - apaga um ídice
    clear - limpa um ídice
    extend - estende a lista
    + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# CRIANDO LISTA
#.........0..1...2...3
lista = [10, 20, 30, 40]
print(lista)

# ADICIONA
lista.append('Luiz')
print(lista)

# REMOVE ÚLTIMO ITEM DA LISTA
nome = lista.pop()
print(lista, nome)

# ADICOAN + DELETA UM ÍNDICE
lista.append(1234)
print(lista)
del lista[-1]
print(lista)

# LIMPA LISTA 
# lista.clear()
# print(lista)

# Usando insert(índice, valor)
lista.insert(0, 5)
print(lista)