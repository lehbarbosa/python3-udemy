"""
Faça um jogo para o usuário adivihar qual
palavra secreta.
- Você vai propor um palavra secreta qualquer
e vai dar a possibilidade para o usuário digitar
apenas um letra.
- Quando o usuário digitar um letra, você vai 
conferir se a letra digitada está na palavra 
secreta.
    - Se a letra digitada estiver na palavra
    secreta; exiba a letra;
    - Se a letra digitada não estiver na 
    palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertada = ''
numero_tentativa = 0
parar = ''
while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativa += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertada += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentivas:', numero_tentativa)
        letras_acertada = ''
        numero_tentativa = 0
        parar = str(input('\nDeseja continuar [S]im ou [N]ão?')).lower()
    
    if parar == 's':
        break