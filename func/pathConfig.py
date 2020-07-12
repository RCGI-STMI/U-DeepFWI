# -*- coding: utf-8 -*-
"""
Path setting
@author: Jonas Mendonca (jonas.mendonca@usp.br)
"""
import os
from func.paramConfig import *

class pathConfig:
  def __init__(self):
    ####################################################
    ####                   FILENAMES               #####
    ####################################################
    self.datafilename  = 'georec'
    self.dataname      = 'rec'
    self.truthfilename = 'vmodel'
    self.truthname     = 'vmodel'
    
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






