from func.paramConfig import param #contains all parameters
from func.pathConfig import path #contains all paths
from func.libConfig import tf,time,loadTrain,create_model,save_time

start  = time.time() 

X_train,Y_train= loadTrain() #loading data

if param.useTransferLearning == True:
    print ('Loading model pre-trained')
    model = tf.keras.models.load_model('models/model.h5') #salva o modelo

else:
    model = create_model() # cria o modelo
    
model.fit(X_train, Y_train, batch_size=param.batchSize, epochs=param.epochs)
model.save('models/modelCurrent.h5')


save_time(time.time() - start);
