from func.paramConfig import param
from func.pathConfig import path
from func.libConfig import *
import warnings
warnings.filterwarnings("ignore")


### PARAMETERS #####
nova_dim= param.modelDimSaida # nova dimensao de acordo com o modelo da rede

test_size = param.testSize
data_dim = param.dataDim
data_dsp_blk = param.data_dsp_blk
label_dsp_blk = param.label_dsp_blk
train_size = param.trainSize
new_dim = param.newDim
model_dim = param.modelDim
in_channels = param.inChannels
start = param.modelInicial
pos = param.posicoes_fonte # posicoes da fonte que eu quero

train_data_dir = param.train_data_dir
folder_dataset = param.folder_dataset

#### FOLDERS ###
datafilename = path.datafilename
dataname = path.dataname
truthfilename = path.truthfilename
truthname = path.truthname


####   LOADING TRAINING  
def loadTrain():
    X_train = np.zeros((train_size, new_dim[0], new_dim[1], in_channels))
    Y_train = np.zeros((train_size, nova_dim[0],nova_dim[1] ,1)) #O y train possui apenas 1 canal

    for i in range(start,start+train_size):
        filename_shot = train_data_dir+folder_dataset[0]+datafilename+str(i)+'.mat'
        data = read_shot(filename_shot,datafilename+str(i),dataname)
        data_shots = add_border_shot(data_dim,in_channels, data,pos)
       
        #Reduzir bloco
        for k in range (0,in_channels):
            aux     = data_shots[:,:,k] #pegando cada shot
            aux_reduzido     = block_reduce(aux,block_size=data_dsp_blk,func=np.max)
            X_train[i-1,:,:,k] = aux_reduzido
        filename_label     = train_data_dir+folder_dataset[1]+truthfilename+str(i)+ '.mat'
        vmodel = read_vmodel(truthfilename+str(i),filename_label,truthname)
        
        Y_train[i-1,:,:,:] = add_border_vmodel(vmodel).reshape(nova_dim[0],nova_dim[1],1)
        X_train = np.float32(X_train)
        
    X_train =processData(X_train)
     
    return X_train,Y_train



#### LOADING TEST
def loadTest():
    
    X_test = np.zeros((test_size, new_dim[0], new_dim[1], in_channels))
    Y_test = np.zeros((test_size, nova_dim[0],nova_dim[1] ,1)) #O y train possui apenas 1 canal
    
       
    cont = 0
    for i in range(train_size+1,train_size+1+test_size): # o conjunto de teste começa depois do treinamento
        
        
        filename_shot = train_data_dir+folder_dataset[0]+datafilename+str(i)+'.mat'
        data = read_shot(filename_shot,datafilename+str(i),dataname)

        data_shots = add_border_shot(data_dim,in_channels, data,pos)
       
        #Reduzir bloco
        for k in range (0,in_channels):
            aux     = data_shots[:,:,k] #pegando cada shot
            aux_reduzido     = block_reduce(aux,block_size=data_dsp_blk,func=np.max)#decimate)
            X_test[cont,:,:,k] = aux_reduzido 
        
        filename_label     = train_data_dir+folder_dataset[1]+truthfilename+str(i)+ '.mat'
        vmodel = read_vmodel(truthfilename+str(i),filename_label,truthname)
        
        Y_test[cont,:,:,:] = add_border_vmodel(vmodel).reshape(nova_dim[0],nova_dim[1],1)
        cont = cont+1
        
    X_test = np.float32(X_test)
       
    X_test =processData(X_test)
    return X_test,Y_test      
 
    
 
    
def read_shot(filename_shot,datafilename,dataname):
    print (datafilename)
    data = sio.loadmat(filename_shot)
    data = data[dataname]
    
    return data
    
def read_vmodel(truthfilename,filename_label,truthname):
    print (truthfilename)
    vmodel          = sio.loadmat(filename_label)
    vmodel          =vmodel[str(truthname)]#.reshape(model_dim)  
    return vmodel


def add_border_vmodel(vmodel):
    aux = vmodel
    aux2 = aux[:,299:300]
    vmodel = np.concatenate((aux,aux2),axis=1)

    aux = vmodel
    aux2 = aux[198:200,:]
    vmodel = np.concatenate((aux,aux2),axis=0)
    vmodel = vmodel[:-1,:]
    
    return vmodel
    
def add_border_shot(data_dim,in_channels, data,pos):
    
    border = 3 #(2000,301) -> (2000,304) replicando as últimas colunas
    data_shots = np.zeros((data_dim[0],data_dim[1],in_channels))
        
    contador=0
    for j in range(0,data.shape[2]):

        if j in pos:
            aux = data[:,:,j]
            aux2 = aux[:,301-border-1:301-1] #adicionando as bordas
            aux3 = np.concatenate((aux,aux2),axis=1)
            data_shots[:,:,contador] = aux3
            contador = contador+1
        
    return data_shots

def processData(data):
    num_channels = data.shape[3]
    num_models = data.shape[0]
    dim = 608
    new_data = np.zeros((num_models,400,dim,1))
    for i in range(num_models):
        shots = data[i] #pegando o conjunto de shots

        for j in range(num_channels):
            
            shot = shots[:,:,j]
            shot2 = shot[:, 1::2]
            
            if j == 0:
                aux = shot2
            else:
                aux = np.concatenate((aux,shot2),axis=1)
        new_data[i] = aux.reshape(400,dim,1)
        
    return new_data
