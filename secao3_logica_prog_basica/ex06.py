"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input('Digite a hora: '))

if hora <= 11:
    print('Bom dia')
if  hora >=12 and hora <=17:
    print('Boa tarde')
if hora >= 18 :
    print('Boa noite')
