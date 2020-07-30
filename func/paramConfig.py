# -*- coding: utf-8 -*-
"""
Parameters setting
@author: Jonas Mendonca (jonas.mendonca@usp.br)
"""
class paramConfig:
  def __init__(self):
    	
    #####       FOLDERS OF DATASETS    ######
    self.train_data_dir = '/home/jonas/Desktop/experiments/'
    self.folder_dataset = ['georec/','vmodel/']

    #####       PARAMETERS OF MODELS   ######
    self.dataDim        = [2000,304]      # Dimension of original one-shot seismic data
    self.newDim         = [400,304]
    self.nclasses       = 1               # Number of output channels
    self.inChannels     = 4               # Number of input channels, number of shots
    self.data_dsp_blk   = (5,1)           # Downsampling ratio of input
    self.modelDim       = [201,301]       # Dimension of one velocity model
    self.modelDimSaida  = [202,302]       # Dimension of output of the network
    self.label_dsp_blk  = (1,1)           # Downsampling ratio of output
    self.positions_source =  [0,10,19,28] # Positions of sources

    ####             NETWORK PARAMETERS             ####
    
    self.useTransferLearning=False	  # Parameter of Transfer Learning
    self.epochs        = 10               # Number of epoch
    self.trainSize     = 10               # Number of training set
    self.testSize      = 10               # Number of testing set
    self.modelInicial  = 1               # Initial model of training
    self.testBatchSize = 5                # Number of batch testing
    self.start_test    = self.trainSize+1 # Position of start Test, you can change manually
    self.batchSize     = 5                # Number of batch size
    self.learnRate     = 1e-3             # Learning rate
   
param = paramConfig() # object param 
