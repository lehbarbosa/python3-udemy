"""
Repetições
while (enquanto)
Executa um ação enquanto uma condição for verdadeira
Loop -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break

print('Acabou!!!')

