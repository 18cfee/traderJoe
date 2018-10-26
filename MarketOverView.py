import numpy
class MarketOverView:
    def __init__(self,CLOSE,lookback):
        self.CLOSE = CLOSE
        self.day = 0
        self.crashState = False
        self.prevMax = 0.0
        self.curDayVal = 0.0
        self.lookback = lookback

    def addDailyData(self,CLOSE):
        self.CLOSE = CLOSE

    def incrementDay(self):
        self.day += 1
        self.prevMax = max(self.curDayVal,self.prevMax)
        self.curDayVal = self.CLOSE.item((self.lookback - 1, 0))
        print(self.prevMax)


    def isInCrashState(self):
        periodLonger = 100
        periodShorter = 10

        smaLongerPeriod = numpy.nansum(self.CLOSE[-periodLonger:, :], axis=0) / periodLonger
        smaShorterPeriod = numpy.nansum(self.CLOSE[-periodShorter:, :], axis=0) / periodShorter

        new = smaShorterPeriod[0]
        old = smaLongerPeriod[0] * .93

        #print("the vars are ", old, new)
        return False
        #return new < old or self.crashState
    def allIn(self):
        pos = numpy.zeros(2)
        pos[0] = 1
        pos[1] = 0
        return pos

    def goCash(self):
        pos = numpy.zeros(2)
        pos[0] = 0
        pos[1] = 1
        return pos
