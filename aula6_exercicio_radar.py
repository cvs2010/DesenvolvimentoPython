"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim) = quanto mais identações longe pior
"""
velocidade = input('Digite sua velocidade (entre 1 e 100): ')  # velocidade atual do carro
velocidade_try1 = velocidade.replace(',','.') #transformando "," em "." se houver
velocidade_float = float(velocidade_try1) #transformando o input em float

local = input('Digite sua posição na estrada(número de 1 a 10): ')  # velocidade atual do carro
local_try1 = local.replace(',','.') #transformando "," em "." se houver
local_float = float(local_try1) #transformando o input em float

RADAR_NAME = 'Radar Móvel'
MAXVEL_RADAR1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 5  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if(LOCAL_1 - RADAR_RANGE <= local_float <= LOCAL_1 + RADAR_RANGE):
    if velocidade_float > MAXVEL_RADAR1:
        print(f'Você excedeu {((velocidade_float) - (MAXVEL_RADAR1)):.0f}km/h da velocidade máxima de {MAXVEL_RADAR1}km/h do {RADAR_NAME}')
    elif velocidade_float < MAXVEL_RADAR1:
        print(f'Você passou {((MAXVEL_RADAR1)- (velocidade_float)):.0f}km/h abaixo da velocidade máxima de {MAXVEL_RADAR1}km/h do {RADAR_NAME}')
else:
    print(f'Você passou muito longe! O {RADAR_NAME} não te detectou!')
    print()