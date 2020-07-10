import os
import scipy.io as sio
from func.paramConfig import param #object with all parameters


def generate_predicoes(predictions,GT): # 
    time_aux = sio.loadmat('./results/time.mat')
    time_aux = time_aux['time']
    data = {}
    data['GT'] = GT
    data['prediction'] = predictions
    data['param'] = param
    data['time_training'] = time_aux
    
    print('SAVING RESULTS')
    sio.savemat('./results/results.mat',data)

def save_time(timec):
    aux_time='Training complete in {:.0f}m  {:.0f}s' .format(timec //60 , timec % 60)
    sio.savemat('./results/time.mat',{'time':aux_time})
