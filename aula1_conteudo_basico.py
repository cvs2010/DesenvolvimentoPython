print(10,11,2023) #Não precisa de aspas para números e nem de +
print(10,11,2023, sep="-", end=".") #Não precisa de aspas para números, o separador = sep, e o enline = end

print() #Colocando um breakline

print("Teste com aspas duplas \"\"") #teste de print de String com aspas duplas e simples é a mesma coisa
print('Teste com aspas simples \'\'')
print(r'Teste de \'caractere de escape') #Caractere de escape primeira alternativa
print('José \'Antônio\'') #Caractere de escape segunda alternativa

# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número positivo ou negativo. int sem sinal é considerado positivo.
print(11) # int
print(-11) # int
print(0)

# float -> Número com ponto flutuante. O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante. Float sem sinal é considerado positivo.
print(1.1, 10.11)
print(0.0, -1.5)

# A função type mostra o tipo que o Python inferiu ao valor.
print(type('Otávio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))

