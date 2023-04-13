"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #adiciona 10 espaços em branco a direita
print(f'{variavel:#>10}') #adiciona 10 # a esquerda
print(f'{variavel:%<10}.') #adiciona 10 % a direita
 #adiciona 10 $ com a mesma quantidade a direita e a esquerda 
print(f'{variavel:$^10}.') #nesse caso só adicionou 3 a esquerda pq sobrou um número ímpar para adicionar
print(f'{1000.4873648123746:.2f}') #arredondando 2 casa decimais
print(f'{1000.4873648123746:,.2f}') #trocando o ponto por espaço
print(f'{1000.4873648123746:+.2f}') #mostrando se é positivo ou negativo
print(f'{1000.4873648123746:0=10.2f}') #colocando zeros a esquerda até ficar com 10 caracteres
print(f'{1000.4873648123746:0=+10.2f}') #adcionando + ou -
print(f'O hexadecimal de 1500 é {1500:08X}') #transformando em HEXADECIMAL
print(f'{variavel!r}')
print()

"""
Fatiamento de strings
    012345678
    Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::]) #normal
print(variavel[::1]) #normal
print(variavel[::-1]) #invertido
print(variavel[2::]) #retirando 2 caracteres a esquerda
print(variavel[:2:]) #apenas pegando os 2 primeiro caracteres a esquerda
print(variavel[:-2:]) #retirando 2 caracteres a direita
print(variavel[-2::]) #apenas pegando os 2 primeiro caracteres a direita
print(variavel[:0:]) #nada (nenhum caractere)
print(len(variavel)) #lenght : quantidade de caracteres da variavel
