""" Calculadora com while """
# while True:
#     num1 = int(input('Digite um número inteiro: '))
#     num2 = int(input('Digite outro número inteiro: '))
#     operador = input('Digite o operador? [+ - * /]: ')

# #Calculos:
#     if operador == '+':
#         soma = num1 + num2
#         print(f'A soma entre: {num1} + {num2} = {soma}')

#     elif operador == '-':
#         subtracao = num1 - num2
#         print(f'A subtração entre: {num1} - {num2} = {subtracao}')

#     elif operador == '*':
#         multiplicacao = num1 * num2
#         print(f'A multiplicação entre: {num1} * {num2} = {multiplicacao}')

#     elif operador == '/':
#         divisao = num1 / num2
#         print(f'A divisão entre: {num1} / {num2} = {divisao:.2f}')


# # Sai do while
#     sair = input('\nQuer sair? [S]im ou [N]ão: ').lower().startswith('s')
#     if sair == True:
#         break


# Resolução da aula:
while True:
    num1 = input('Digite um número inteiro: ')
    num2 = input('Digite outro número inteiro: ')
    operador = input('Digite o operador? [+ - * /]: ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
   
    operadores_permitidos = '+-*/'
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        soma = num1_float + num2_float
        print(f'{num1_float} + {num2_float} = {soma}')

    elif operador == '-':
        subtracao = num1_float - num2_float
        print(f'{num1_float} - {num2_float} = {subtracao}')

    elif operador == '*':
        multiplicacao = num1_float * num2_float
        print(f'{num1_float} * {num2_float} = {multiplicacao}')

    elif operador == '/':
        divisao = num1_float / num2_float
        print(f'{num1_float} / {num2_float} = {divisao:.2f}')

    sair = input('\nQuer sair? [S]im ou [N]ão: ').lower().startswith('s')
    if sair == True:
        break
