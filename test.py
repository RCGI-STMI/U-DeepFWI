from func.paramConfig import param #objeto contendo todos os parametros
from func.pathConfig import path #objeto contendo todos os parametros
from func.libConfig import *

X_test,Y_test = loadTest() #loading data

model = tf.keras.models.load_model('models/modelCurrent.h5')

preds_test = model.predict(X_test, batch_size=param.testBatchSize)

generate_predicoes(preds_test,Y_test)