!pip install pandas

import pandas as pd 
import numpy as np
import math
import random


import pandas as pd
FILE_NAME = '/Users/elranshahar/vehicleAPI/Shifts_6.0/Shifts Submission - Sheet1.csv'

file = pd.read_csv(FILE_NAME)

def fileToObject(file):
    output ={}
    fileCoulumns = file.columns
    workersNames = list(file['Names'])
    for i in workersNames:
        output[i] = {}
        for j in fileCoulumns:
            if j != 'Names':
                output[i][j] = file[j][workersNames.index(i)]

    return output




class GenerateShiftsData:
    
    def __init__(self) -> None:
        pass

    def getWorkers(self):
        return list(file['Names'])

    def getShifts(self):
        return list(file.columns)[1:]

    def getWorkersShifts(self):
        return fileToObject(file)
    

    















# Path: Shifts_6.0/shifts.py


