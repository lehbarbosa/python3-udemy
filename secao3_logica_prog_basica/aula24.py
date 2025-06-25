"""
Formação básica de strings
s - strings
d - int
f - float
. <números de digitos>f
x ou X hexadeciamal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita 
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.f
Conversion flags - !r !s !a   
 """
variavel = 'ABC'
print(f'{variavel}') 
print(f'{variavel: >10}') 
print(f'{variavel: <10}') 
print(f'{variavel: ^10}') 
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
