import numpy as np
import numpy.random as rnp
import pandas as pd
import pdb
#https://www.frontiersin.org/articles/10.3389/fnins.2019.00413/full
stimAmplitudes = [10,15,20,25,30]
maxFiring = [50.,75.,80.,100.,125.]
standardDev = 20
numElectrodes = 16
Electrodes = range(numElectrodes)
numReps = 10
totalStimAmps = []
totFiringRate = []
electrodeList = []
animalID = []
numAnimals = 10
for cmk in range(numAnimals):
    for ck in range(numReps):
        for bc in range(numElectrodes):
            for jk in range(len(stimAmplitudes)):
                totalStimAmps.append(stimAmplitudes[jk])
                electrodeList.append(Electrodes[bc])
                totFiringRate.append(rnp.normal(loc =maxFiring[jk], scale=standardDev))
                animalID.append(cmk)
data = {'stimAmp':totalStimAmps,
        'electrode':electrodeList,
        'animalID':animalID,
        'maxFiring':totFiringRate}
df = pd.DataFrame(data)
df.to_csv('sampleNeuralData.csv')
