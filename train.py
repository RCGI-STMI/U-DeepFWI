from func.paramConfig import param #contains all parameters
from func.libConfig import tf,time,loadTrain,create_model,save_time

start = time.time()

X_train,Y_train= loadTrain() #loading data

tf.debugging.set_log_device_placement(True)
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    if param.useTransferLearning == True:
        print('LOADING MODEL PRE-TRAINED')
        model = tf.keras.models.load_model('models/model.pb') #Applying Tranfer learning
    else:
        model = create_model()
    
model.fit(X_train, Y_train, batch_size=param.batchSize, epochs=param.epochs)
print('SAVING MODEL')
model.save('models/modelCurrent.pb')

final_time = time.time() - start
save_time(final_time)
