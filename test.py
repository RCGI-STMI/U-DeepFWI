from func.paramConfig import param #object with parameters
from func.pathConfig import path #object with path
from func.libConfig import tf,loadTest,generate_predicoes

X_test,Y_test = loadTest() #loading data

model = tf.keras.models.load_model('models/modelCurrent.h5')

preds_test = model.predict(X_test, batch_size=param.testBatchSize)

generate_predicoes(preds_test,Y_test)