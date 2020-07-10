# -*- coding: utf-8 -*-
"""
Path setting
@author: Jonas Mendonca (jonas.mendonca@usp.br)
"""

import os
from func.paramConfig import *

####################################################
####                   FILENAMES               #####
####################################################

# Data filename
tagD0 = 'georec'
tagV0 = 'vmodel'
tagD1 = 'rec'
tagV1 = 'vmodel'

datafilename  = tagD0
dataname      = tagD1
truthfilename = tagV0
truthname     = tagV1


class pathConfig:
  def __init__(self):
    self.datafilename  = tagD0
    self.dataname      = tagD1
    self.truthfilename = tagV0
    self.truthname     = tagV1
    
    ###################################################
    ####                   PATHS                  #####
    ###################################################
    self.main_dir = './'
    
    ## Create Results and Models path
    if os.path.exists('./results/'):
        self.results_dir     = self.main_dir + 'results/' 
    if os.path.exists('./models/'):
        self.models_dir      = self.main_dir + 'models/'
    else:
        os.makedirs('./results/')
        os.makedirs('./models/')
        self.results_dir     = self.main_dir + 'results/'
        self.models_dir      = self.main_dir + 'models/'


    if os.path.exists(self.results_dir) and os.path.exists(self.models_dir):  
        self.results_dir     = self.results_dir
        self.models_dir      = self.models_dir 
    else:
        os.makedirs(self.results_dir)
        os.makedirs(self.models_dir)
        self.results_dir     = self.results_dir
        self.models_dir      = self.models_dir



path = pathConfig() # objeto utilizado para pegar o dado






