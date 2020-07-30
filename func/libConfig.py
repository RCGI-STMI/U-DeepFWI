# -*- coding: utf-8 -*-
"""
Import libraries
@author: Jonas Mendonca (jonas.mendonca@usp.br)
"""

################################################
########            LIBRARIES            ########
################################################

import warnings
import os,sys
import time
sys.path.append(os.getcwd())
import numpy as np
import scipy.io as sio
from skimage.measure import block_reduce

###### Imports of Tensorflow and keras #####
import tensorflow as tf
from tensorflow.keras.models import Model#Sequential, Model
from tensorflow.keras.layers import MaxPooling2D, Conv2D, BatchNormalization,Activation, Conv2DTranspose, Input, concatenate, Cropping2D
from tensorflow.keras.models import Model, load_model



###### Import Functions #####
from func.libsJ import generate_predicoes, save_time
from func.loadData import loadTrain, loadTest
from func.model import create_model
