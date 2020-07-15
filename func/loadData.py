from func.paramConfig import param 
from func.pathConfig import path
from func.libConfig import np,block_reduce, sio
import warnings
warnings.filterwarnings("ignore")

####   LOADING TRAINING  
def loadTrain():
    X_train,Y_train = create_matrix(param.trainSize)

    for i in range(param.modelInicial,param.modelInicial+param.trainSize):
        position= i-1 # to solve the problem of python start with zero
        X_train = get_shot(i,position,X_train)
        vmodel = read_vmodel(i)
        Y_train[position,:,:,:] = vmodel
    X_train = np.float32(X_train)  
    X_train =processData(X_train)
    return X_train,Y_train

#### LOADING TEST
def loadTest():
    X_test,Y_test = create_matrix(param.testSize)
    position = 0

    for i in range(param.trainSize+1,param.trainSize+1+param.testSize): # The test size start after the training       
        X_train = get_shot(i,position,X_test)   
        vmodel = read_vmodel(i)
        Y_test[position,:,:,:] = vmodel
        position +=1
    X_test = np.float32(X_test)
    X_test =processData(X_test)
    return X_test,Y_test  

### READ EACH VMODEL
def read_vmodel(i):
    filename_label     = param.train_data_dir+param.folder_dataset[1]+path.truthfilename+str(i)+ '.mat'
    print (path.truthfilename+str(i))
    vmodel          = sio.loadmat(filename_label)
    vmodel          =vmodel[str(path.truthname)]
    vmodel = add_border_vmodel(vmodel).reshape(param.modelDimSaida[0],param.modelDimSaida[1],1)
    return vmodel

### READ EACH SHOT
def get_shot(i,position,dataset):
    filename_shot = param.train_data_dir+param.folder_dataset[0]+path.datafilename+str(i)+'.mat'
    data = read_shot(filename_shot,path.datafilename+str(i),path.dataname)
    shots = add_border_shot(param.dataDim,param.inChannels, data)
    dataset =apply_block_reduce(dataset,shots,position)
   
    return dataset;

def apply_block_reduce(X_train,shots,position):#Block reduce
    for k in range (0,param.inChannels):
        shot_k= shots[:,:,k] # getting each shot
        aux= block_reduce(shot_k,block_size=param.data_dsp_blk,func=np.max)
        X_train[position,:,:,k] = aux
    return X_train

def create_matrix(size_matrix): # create the null matrix
    X = np.zeros((size_matrix, param.newDim[0], param.newDim[1], param.inChannels))
    Y = np.zeros((size_matrix, param.modelDimSaida[0],param.modelDimSaida[1] ,1)) #O y train possui apenas 1 canal
    return X,Y 
 
def read_shot(filename_shot,datafilename,dataname):
    print (datafilename)
    data = sio.loadmat(filename_shot)
    data = data[dataname]
    return data
    
def add_border_vmodel(vmodel): # reshape vmodel (201,301) -> (202,302)
    border =1
    vmodel = np.concatenate((vmodel,vmodel[:,-border:]),axis=1)
    vmodel = np.concatenate((vmodel,vmodel[-border:,:]),axis=0)
    return vmodel
    
def add_border_shot(data_dim,in_channels, data): #(2000,301) -> (2000,304) replying the last columns
    border = 3 
    data_shots = np.zeros((data_dim[0],data_dim[1],in_channels))
    contador=0

    for j in param.positions_source : # Selecting only shots equals positions, in our case we use 29 shots and selecting only 4 shots equispaced in domain
        aux = data[:,:,j]
        data_shots[:,:,contador] = np.concatenate((aux,aux[:,-border:]),axis=1)
        contador +=1
    return data_shots

def processData(data): #resize each set of shot to (400,608)
    num_channels = data.shape[3]
    num_models = data.shape[0]
    dim1 = data.shape[1]
    dim2 = 608
    new_data = np.zeros((num_models,dim1,dim2,1))
    for i in range(num_models):
        shots = data[i]
        for j in range(num_channels):
            shot = shots[:,1::2,j]
            if j == 0:
                aux = shot
            else:
                aux = np.concatenate((aux,shot),axis=1)
        new_data[i] = aux.reshape(dim1,dim2,1)
    return new_data
