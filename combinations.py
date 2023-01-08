from itertools import permutations
from itertools import product
import random
from settings import GenerateShiftsData


data = GenerateShiftsData()
shifts = data.getShifts()
workers = data.getWorkers()
workersShifts = data.getWorkersShifts()
def getShiftsByWorker(worker):
    return workersShifts[worker]

def getWorkersByShiftAs3(shift):
    output = []
    for i in workers:
        if getShiftsByWorker(i)[shift] == 3:
            output.append(i)
    return output

def getWorkersByShiftAs2(shift):
    output = []
    for i in workers:
        if getShiftsByWorker(i)[shift] == 2:
            output.append(i)
    return output

def mergeLists(list1, list2):
    output = []
    for i in list1:
        output.append(i)
    for i in list2:
        output.append(i)
    return output


class Combinations:

    def __init__(self):
        self.options = {}

    
    def createOptions(self):
        options = {}
        for i in range(len(shifts)):
            options[shifts[i]] = mergeLists(getWorkersByShiftAs3(shifts[i]),getWorkersByShiftAs2(shifts[i]))
        self.options = options
        return self.options
    
    def createAllCombinations(self):
        schedules = []
        limit = 300 
        shifts  = list(self.options.keys())
        employees = [employees for employees in self.options.values()]
        for schedule in product(*self.options.values()):
            schedules.append(list(zip(shifts,schedule)))
            print(schedules)
            print ("limit", limit)
            limit -= 1
            if limit == 0:
                print("limit", limit)
                break
        print(len(schedules))
        return schedules

        
    



            