"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    numero_try1 = numero_str.replace(',','.') #transformando "," em "." se houver
    numero_float = float(numero_try1) #transformando o input em float
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_float:.2f} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número') #se o usuário não digitar um número válido retorna isso

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')