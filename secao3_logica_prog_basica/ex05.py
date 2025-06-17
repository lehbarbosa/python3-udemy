"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_inteiro = int(input('Digite um númeiro inteiro: '))

if (numero_inteiro % 2) == 0:
    print(f'O número {numero_inteiro} é PAR')
else:
    print(f'O número {numero_inteiro} é Ímpar')
