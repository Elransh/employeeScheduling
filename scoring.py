from workers import Worker

elranWorker = Worker('Elran', {'morning': 3, 'evening': 3, 'night': 3})
elranWorker
print(elranWorker.info)

print(elranWorker.createInitialInfo())

print(elranWorker.info)

print(elranWorker.getWorkerEntities())


class Scorer:
    from workers import Worker
    def __init__(self, workerInfo, shift):
        self.workerInfo = workerInfo
        self.shift = shift
        self.score = 0

    def getScore(self):
        return self.score
    
    def calcScoreOnLatestShift(self):
        latestShift = self.workerInfo.getInfoEntity('last_shift')
        print(latestShift)






class ScheduleScorer:

    def __init__(self, schedule):
        self.schedule = schedule
    


elranScore  = Scorer(elranWorker, "shift")
elranScore.calcScoreOnLatestShift()
