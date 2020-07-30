import os
import scipy.io as sio
from datetime import datetime
from func.paramConfig import param #object with all parameters


def generate_predicoes(predictions,GT,time_test): #
    time_training = sio.loadmat('./results/time.mat') #import time of the training
    time_training = time_training['time']
    data = {}
    data['GT'] = GT
    data['prediction'] = predictions
    data['param'] = param
    data['date'] = datetime.now().isoformat()
    data['time_training'] = time_training #save the time of the training
    data['time_testing'] = get_time_test(time_test) #save the time of the testing too

    
    print('SAVING RESULTS')
    sio.savemat('./results/results.mat',data)


def get_time_test(timec):
    return 'Testing complete in {:.0f}m  {:.0f}s'.format(timec // 60, timec % 60)

def save_time(timec):
    aux_time='Training complete in {:.0f}m  {:.0f}s' .format(timec //60 , timec % 60)
    sio.savemat('./results/time.mat',{'time':aux_time})

