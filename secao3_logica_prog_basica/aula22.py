# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])

# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome =input('Digite seu nome: ')
encontar = input('Digite o que deseja encontrar: ')

if encontar in nome:
    print(f'{encontar} está em {nome}')
else:
    print(f'{encontar} não está em {nome}')