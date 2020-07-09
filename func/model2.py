"""
Created on Fri Apr 10 03:09:07 2020
@author: jonas
"""
from func.libConfig import *
from func.paramConfig import param

linhas=param.newDim[0]
colunas=608
canais=1

def apply_maxPooling(camada):
    camada = MaxPooling2D(pool_size=(2,2),padding='same') (camada)
    return camada

def reduzir(camada,out_size):
    camada = Conv2D(filters=out_size, kernel_size=(3, 3), input_shape=(linhas, colunas, canais), strides=1, padding='same') (camada)
    camada = BatchNormalization() (camada)
    camada = Activation('relu') (camada)
    
    camada = Conv2D(filters=out_size, kernel_size=(3, 3), input_shape=(linhas, colunas, canais), strides=1, padding='same') (camada)
    camada = BatchNormalization() (camada)
    camada = Activation('relu') (camada)
    
    return camada


def reduzir_last(camada,out_size):
    camada = Conv2D(filters=out_size, kernel_size=(3, 3), input_shape=(linhas, colunas, canais), strides=1, padding='same') (camada)
    camada = BatchNormalization() (camada)
    camada = Activation('relu') (camada)

    return camada

def aumentar_last(camada_corrente,camada_de_reducao_correspondente,out_size):
    camada = Conv2DTranspose(filters=out_size,kernel_size=(2,2),strides=2,padding='same') (camada_corrente)
    camada = concatenate([camada,camada_de_reducao_correspondente],axis=3) #concatenate of layers
    camada = reduzir_last(camada,out_size)

    return camada


def aumentar(camada_corrente,camada_de_reducao_correspondente,out_size):
    camada = Conv2DTranspose(filters=out_size,kernel_size=(2,2),strides=2,padding='same') (camada_corrente)
    camada = concatenate([camada,camada_de_reducao_correspondente],axis=3) #concatenate of layers
    camada = reduzir(camada,out_size)

    return camada


def create_model2():
    inputs = Input((linhas,colunas,canais))
    
    filtros=[16,32,64,128,512]
#     filtros=[64,128,256,512,1024]
    c1 = reduzir(inputs,filtros[0])
    c2 = reduzir(apply_maxPooling(c1),filtros[1])
    c3 = reduzir(apply_maxPooling(c2),filtros[2])
    c4 = reduzir(apply_maxPooling(c3),filtros[3])
    c5 = reduzir(apply_maxPooling(c4),filtros[4])
    

    c6 = aumentar(c5,c4,filtros[3])
    c7 = aumentar(c6,c3,filtros[2])
    c8 = aumentar(c7,c2,filtros[1])
    c9 = aumentar_last(c8,c1,filtros[0])
    
    c9 = Cropping2D(cropping=(99, 153)) (c9) #fiz um crop na imagem que era (400,304) e deixei com (202,302)
    c9 = reduzir_last(c9,filtros[0])
    c9 = Conv2D(filters=1, kernel_size=(1, 1), strides=1) (c9)

    model = Model(inputs=[inputs],outputs=[c9])
    model.compile(optimizer='adam', loss='mse', metrics=['mse'])
    model.summary()
    return model