"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índice e fatiamento
Métodos úteis - append, insert, pop, del, clear, extende, +
Create, Read, Update, Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
lista[2] = 300
# print(lista)
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50)
print(lista)
lista.pop()
print(lista)
lista.append(60)
print(lista)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)
