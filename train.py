from func.paramConfig import param #objeto contendo todos os parametros
from func.pathConfig import path #objeto contendo todos os parametros
from func.libConfig import *

start  = time.time()

X_train,Y_train= loadTrain() #loading data

if param.useTransferLearning == True:
    print ('Loading model pre-trained')
    model = tf.keras.models.load_model('models/model.h5') #salva o modelo

else:
    model = create_model2() # cria o modelo
    
model.fit(X_train, Y_train, batch_size=param.batchSize, epochs=param.epochs)
model.save('models/modelCurrent.h5')


save_time(time.time() - start);
