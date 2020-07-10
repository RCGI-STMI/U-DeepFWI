# -*- coding: utf-8 -*-
"""
Import libraries
@author: Jonas Mendonca (jonas.mendonca@usp.br)
"""

################################################
########            LIBRARIES            ########
################################################

import random
import warnings
import os, sys
import  time
sys.path.append(os.getcwd())
import numpy as np
import scipy.io as sio
import matplotlib
matplotlib.use('Agg')
from skimage.io import imread, imshow, imread_collection, concatenate_images
from skimage.measure import block_reduce
from scipy import stats

###### Imports of Tensorflow and keras #####
import tensorflow as tf
from tensorflow.keras.models import Model#Sequential, Model
from tensorflow.keras.layers import MaxPooling2D, Conv2D, BatchNormalization,Activation, Conv2DTranspose, Input, concatenate, Cropping2D
from tensorflow.keras import backend as K
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import optimizers


###### Import of the Functions #####
from func.libsJ import generate_predicoes, save_time
from func.loadData import loadTrain, loadTest
from func.model import create_model
