
import itertools
import random

class Worker:

    def __init__(self, worker, requestsDictionary):
        self.worker = worker
        self.requests = requestsDictionary
        self.info = {}

    def createInitialInfo(self): # Create the initial info dictionary
        output = {}
        output['night_shifts_until_shift'] = 0
        output['max_night_shifts'] = 0
        output['max_shifts'] = 0
        output['shifts_until_shift'] = 0
        output['night_shifts_until_shift'] = 0
        output['last_shift'] = 0 
        output['last_night_shift'] = 0
        output['amount_of_shifts_morning_requested_as_3'] = 0
        output['amount_of_shifts_morning_requested_as_2'] = 0
        output['amount_of_shifts_morning_requested_as_1'] = 0
        output['amount_of_shifts_evening_requested_as_3'] = 0
        output['amount_of_shifts_evening_requested_as_2'] = 0
        output['amount_of_shifts_evening_requested_as_1'] = 0
        output['amount_of_shifts_night_requested_as_3'] = 0
        output['amount_of_shifts_night_requested_as_2'] = 0
        output['amount_of_shifts_night_requested_as_1'] = 0
        output['amount_of_morning_shifts_got'] = 0
        output['amount_of_evening_shifts_got'] = 0
        self.info = output
        return {"status": "success in creating initial info dictionary"}
    
    def getWorkerEntities(self):
        return self.info.keys()
    
    def updateInfoEntity(self, entity, value):
        self.info[entity] = value
        return {"status": "success in updating info entity"}
    
    def addInfoEntity(self, entity, value):
        self.info[entity] = value
        return {"status": "success in adding info entity"}
    
    def additionToInfoEntity(self, entity, value):
        self.info[entity] += value
        return {"status": "success in adding to info entity"}
    
    def subtractionFromInfoEntity(self, entity, value):
        self.info[entity] -= value
        return {"status": "success in subtracting from info entity"}
    
    def removeInfoEntity(self, entity):
        self.info.pop(entity)
        return {"status": "success in removing info entity"}
    
    
    def getInfoEntity(self, entity):
        return self.info[entity]
    
    def getWorker(self):
        return self.worker
    

    





    
        
        
    

    
    





# Path: Shifts_6.0/workerCombinations.py

