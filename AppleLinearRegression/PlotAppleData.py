file = "..\\tickerData\\AAPL.txt"
import matplotlib.pyplot as plt
rateDates = []
rates = []
with open(file, 'r') as f:
    text = f.read()
    lines = text.splitlines()
    pricesClose = []
    dates = []
    size = []
    for line in lines[1:]:
        line = line.split(',')
        pricesClose.append(float(line[4]))
        dates.append(int(line[0]))
        size.append(.5)
    # for i in range(len(dates)):
    #     print "date:" , dates[i] , "price:" , pricesClose[i]
    points = range(len(dates))
    # plt.scatter(points, pricesClose, s=size, alpha=1)
    # plt.show()

    rateDates = dates[1:]
    prevPrice = pricesClose[0]
    for price in pricesClose[1:]:
        rate = (price - prevPrice)/price
        prevPrice = price
        rates.append(rate)
    # for i in range(len(rateDates)):
    #     if(abs(rates[i]) > .1):
    #         print "date:" , rateDates[i] , "price:" , rates[i]
    points = range(len(rateDates))
    size = []
    for i in range(len(rateDates)):
        size.append(.5)
    # plt.scatter(points,rates, s=size)
    # plt.show()


datafile = "..\\CorrelationCalculator\\data.csv"
dates = set()
data = []
with open(datafile, 'r') as f:
    text = f.read()
    lines = text.splitlines()
    previousLine = lines[1].split(',')
    for i in range(len(previousLine))[1:]:
        if previousLine[i] == '':
            previousLine[i] = -724
    for line in lines[2:]:
        line = line.split(',')
        for i in range(len(line))[1:]:
            if line[i] == '':
                line[i] = previousLine[i]
        dates.add(int(line[0]))
        dataRates = []
        for i in range(len(line))[1:]:
            prevVal = float(previousLine[i])
            curVal = float(line[i])
            rate = (curVal - prevVal)/(curVal + .000000001)
            if prevVal == 724:
                rate = 0
            data.append(rate)
        data.append(dataRates)
        previousLine = line

datesList = []
filteredRates = []
print(dates)
for i in range(len(rateDates)):
    date = rateDates[i]
    rate = rates[i]
    if date in dates:
        datesList.append(date)
        filteredRates.append(rate)
        print date , rate

plt.scatter(range(len(filteredRates)),filteredRates)
plt.show()




