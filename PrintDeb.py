import numpy
class PrintDeb:
    def allPrinting(self,settings,CLOSE,on):
        if(not on):
            return
        nMarkets = CLOSE.shape[1]
        print("the number of markets ", nMarkets)

        periodLonger = 100
        periodShorter = 10

        # Calculate Simple Moving Average (SMA)

        if ('testField' not in settings.keys()):
            print("not in yet")
            settings['testField'] = 1
        else:
            settings['testField'] += 1
            print("it is in now value hea: ", settings['testField'])

        smaLongerPeriod = numpy.nansum(CLOSE[-periodLonger:, :], axis=0) / periodLonger
        smaShorterPeriod = numpy.nansum(CLOSE[-periodShorter:, :], axis=0) / periodShorter
        print("smaLonger ", smaLongerPeriod)
        print("smaShorter ", smaShorterPeriod)
        longEquity = smaShorterPeriod > smaLongerPeriod
        print("long is: ", longEquity)
        shortEquity = ~longEquity
        print("short is: ", shortEquity)
        pos = numpy.zeros(nMarkets)

        pos[longEquity] = settings['testField'] % 2 * 0
        pos[shortEquity] = settings['testField'] % 2 * 0
