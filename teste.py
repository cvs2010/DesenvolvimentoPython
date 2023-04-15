from keras.models import load_model
import numpy as np
import cv2

#importando imagem
imagem = cv2.imread('C:/Dev/Projects/Python/curso_python_udemy/imagem1.jpg')
imagem_redimensionada = cv2.resize(imagem, (150, 150))

# Carrega o modelo salvo no formato .h5
modelo = load_model('C:\Dev\Projects\Python\curso_python_udemy\modelo.h5')


# Definindo a variável novos_dados para receber os dados do predict
novos_dados = np.array([imagem_redimensionada, imagem_redimensionada, imagem_redimensionada, imagem_redimensionada, imagem_redimensionada])

# Faz previsões em novos dados
previsoes = modelo.predict(novos_dados)

#Dando um print da previsão do model
print(previsoes)


#salvando o modelo.h5 em JSON para leitura do Tensorflow
import tensorflow as tf

# Salva o modelo em formato SavedModel
tf.saved_model.save(modelo, os.path.join('C:', 'Dev', 'Projects', 'Python', 'curso_python_udemy', 'saved_model'))

# Converte o modelo em formato SavedModel para JSON usando o tensorflowjs_converter
!tensorflowjs_converter --input_format=tf_saved_model --output_format=tfjs_graph_model {os.path.join('C:', 'Dev', 'Projects', 'Python', 'curso_python_udemy', 'saved_model')} {os.path.join('C:', 'Dev', 'Projects', 'Python', 'curso_python_udemy', 'model')}
