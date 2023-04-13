"""
# if / elif  / else:
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else: #atenção o else tem que ter ":" depois dele "else:"
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')
print()
"""

"""
# Teste trocar os trues por falses e veja o que acontece
senha1 = True
senha2 = True
senha3 = True
senha4 = True

if senha1:
    print('Acertou a senha 1')
    print('Código para condição 1')
if senha2:
    print('Acertou a senha 2')
if senha3:
    print('Acertou a senha 3')
elif senha4:
    print('Acertou a senha 4')
else:
    print('Não acertou nenhuma senha.')

if 10 == 10:
    print('Outro if')

print('Fora do if')
print()

"""

"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(maior, maior_ou_igual, menor, menor_ou_igual, igual, diferente)
print()

"""



# Criando um sistema de login simples
# Operadores lógicos and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu) 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor
entrada = input('Digite [E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

#Duas formas de checar esse login
# if (entrada in ['e','E']) and senha_digitada == senha_permitida:
if (entrada == 'e' or entrada=='E') and senha_digitada == senha_permitida:
    print('Você logou no Sistema')
else:
    print('Falha na tentativa de Logina')

print()