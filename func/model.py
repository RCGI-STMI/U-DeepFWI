"""
Created on Fri Apr 10 03:09:07 2020
@author: jonas
"""
from func.libConfig import MaxPooling2D, Conv2D,Activation,BatchNormalization,concatenate,Conv2DTranspose,Input,Cropping2D, Model
from func.paramConfig import param

rows=param.newDim[0]
columns=608
channels=param.nclasses

def apply_maxPooling(layer):
    layer = MaxPooling2D(pool_size=(2,2),padding='same') (layer)
    return layer

def reduce(layer,out_size):
    layer = Conv2D(filters=out_size, kernel_size=(3, 3), input_shape=(rows, columns, channels), strides=1, padding='same') (layer)
    layer = BatchNormalization() (layer)
    layer = Activation('relu') (layer)
    
    layer = Conv2D(filters=out_size, kernel_size=(3, 3), input_shape=(rows, columns, channels), strides=1, padding='same') (layer)
    layer = BatchNormalization() (layer)
    layer = Activation('relu') (layer)
    
    return layer


def reduce_last(layer,out_size):
    layer = Conv2D(filters=out_size, kernel_size=(3, 3), input_shape=(rows, columns, channels), strides=1, padding='same') (layer)
    layer = BatchNormalization() (layer)
    layer = Activation('relu') (layer)

    return layer

def increase_last(current_layer,layer_of_reduction_correspondent,out_size):
    layer = Conv2DTranspose(filters=out_size,kernel_size=(2,2),strides=2,padding='same') (current_layer)
    layer = concatenate([layer,layer_of_reduction_correspondent],axis=3) #concatenate of layers
    layer = reduce_last(layer,out_size)

    return layer


def increase(current_layer,layer_of_reduction_correspondent,out_size):
    layer = Conv2DTranspose(filters=out_size,kernel_size=(2,2),strides=2,padding='same') (current_layer)
    layer = concatenate([layer,layer_of_reduction_correspondent],axis=3) #concatenate of layers
    layer = reduce(layer,out_size)

    return layer


def create_model():
    inputs = Input((rows,columns,channels))
    
    vet_filters=[16,32,64,128,512]

    c1 = reduce(inputs,vet_filters[0])
    c2 = reduce(apply_maxPooling(c1),vet_filters[1])
    c3 = reduce(apply_maxPooling(c2),vet_filters[2])
    c4 = reduce(apply_maxPooling(c3),vet_filters[3])
    c5 = reduce(apply_maxPooling(c4),vet_filters[4])
    

    c6 = increase(c5,c4,vet_filters[3])
    c7 = increase(c6,c3,vet_filters[2])
    c8 = increase(c7,c2,vet_filters[1])
    c9 = increase_last(c8,c1,vet_filters[0])
    
    c9 = Cropping2D(cropping=(99, 153)) (c9) # crop of (400,304) to (202,302)
    c9 = reduce_last(c9,vet_filters[0])
    c9 = Conv2D(filters=1, kernel_size=(1, 1), strides=1) (c9)

    model = Model(inputs=[inputs],outputs=[c9])
    model.compile(optimizer='adam', loss='mse', metrics=['mse'])
    model.summary()
    return model
