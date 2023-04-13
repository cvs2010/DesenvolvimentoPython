print(10,11,2023) #Não precisa de aspas para números e nem de +
print(10,11,2023, sep="-", end=".") #Não precisa de aspas para números, o separador = sep, e o enline = end

print() #Colocando um breakline

print("Teste com aspas duplas \"\"") #teste de print de String com aspas duplas e simples é a mesma coisa
print('Teste com aspas simples \'\'')
print(r'Teste de \'caractere de escape') #Caractere de escape primeira alternativa
print('José \'Antônio\'') #Caractere de escape segunda alternativa
print()

# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número positivo ou negativo. int sem sinal é considerado positivo.
print(11) # int
print(-11) # int
print(0)
print()

# float -> Número com ponto flutuante. O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante. Float sem sinal é considerado positivo.
print(1.1, 10.11)
print(0.0, -1.5)
print()

# A função type mostra o tipo que o Python inferiu ao valor.
print(type('Otávio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))
print()

# Tipo de dado bool (boolean)
# Ao questionar algo em um programa, só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que questiona se um valor é igual a outro
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))
print()

# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# É o ato de converter um tipo em outro tipo imutável e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print((float('1') + 1))
# print(('1' + 1)) = isso é um erro, não pode somar String '1' com número 1
print(bool(' '))
print(str(11) + 'b')
print()

# Variáveis são usadas para salvar algo na memória do computador. (letra minúscula)
# Constantes salvam registros, porém imutáveis, no Python são identificadas com LETRA MAIÚSCULA
nome = 'José'
idade = 17
MAIOR_DE_IDADE = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior de idade?', maior_de_idade)
print()

#Exercício básico para criação de variáveis
nome = 'José'
sobrenome = 'da Silva'
data_de_nascimento = '11-05-1990'
idade = 19
altura = 1.80
peso = (65.8, 'kg')
eh_maior_de_idade = idade >= 18

print('Nome:', nome , sobrenome)
print('Data de nascimento:' , data_de_nascimento, ', idade:' , idade)
print('Altura:', altura, 'peso:', peso)
print('É maior de idade?', eh_maior_de_idade)
print()

#Operadores matemáticos em python
adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3 # divisão inteira com duas barras
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10 # exponenciação é dois ** e não ^
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão em módulo
# com isso dá para saber que um número é par ou ímpar
print('Módulo', modulo)

print('10 % 8 é maior que 0', 10 % 8, 10 % 8 > 0, sep="-")
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)
print()

#Concatenação e operadores matemáticos, repetindo uma String
concatenacao = 'José' + ' ' + 'Antônio'
print(concatenacao)

a_dez_vezes = 'A' * 10
print(a_dez_vezes)
print(3 * 'Luíz')
print()

#Exercício do IMC
nome = 'José Antônio'
altura = (1.80)
peso = 95
imc = round(peso / altura ** 2,2) #arredondando para duas casas decimais

print(nome, 'tem', altura, 'de altura e pesa',peso, 'quilos')
print('Seu imc é',imc)
print()

#Formatação de números e Strings
"f-strings"
linha_1 = f'{nome} tem {altura:.2f}m de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)
print()

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
print()

