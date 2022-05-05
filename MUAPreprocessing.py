#-------------------------------------------------------------------------------
# Sample datapreprocessing function for Bayesian Heirarchical Linear Regression
# Sample 16 channel evoked responses
#-------------------------------------------------------------------------------
import numpy as np
def MUAPreprocessing(data):
    stimAmp = data["stimAmp"] #Predictor
    maxFiringRate = data["maxFiring"]   #Data
    electrodes = len(data["electrode"])    #Ngroups
    animalIDX = data['animalID']    #Subject IDX
    return [stimAmp,maxFiringRate,animalIDX,electrodes]