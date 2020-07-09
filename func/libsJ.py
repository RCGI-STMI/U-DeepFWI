import os
import scipy.io as sio
from func.paramConfig import param #objeto contendo todos os parametros
from func.pathConfig import path #objeto contendo todos os path


def generate_predicoes(predicoes,GT): # passo as predicoes e os Ground Truths
    tempo = sio.loadmat('./results/tempo.mat')
    tempo = tempo['tempo']
    data = {}
    data['GT'] = GT
    data['prediction'] = predicoes
    data['param'] = param
    data['time_training'] = tempo
    
    print('SAVING RESULTS')
    sio.savemat('./results/results.mat',data)

def save_time(tempo):
    tempo='Training complete in {:.0f}m  {:.0f}s' .format(tempo //60 , tempo % 60)
    sio.savemat('./results/tempo.mat',{'tempo':tempo})