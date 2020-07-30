from func.paramConfig import param #object with parameters
from func.pathConfig import path #object with path
from func.libConfig import tf,loadTest,generate_predicoes,time

start  = time.time()

X_test,Y_test = loadTest() #loading data

tf.debugging.set_log_device_placement(True)
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    model = tf.keras.models.load_model('models/modelCurrent.pb')
preds_test = model.predict(X_test, batch_size=param.testBatchSize)

final_time = time.time() - start
generate_predicoes(preds_test,Y_test,final_time)