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


    os.makedirs('./results/', exist_ok=True)
    os.makedirs('./models/', exist_ok=True)
    self.results_dir     = self.main_dir + 'results/'
    self.models_dir      = self.main_dir + 'models/'

path = pathConfig() # objeto utilizado para pegar o dado






