file = "..\\tickerData\\AAPL.txt"
import matplotlib.pyplot as plt
# rateDates = dates[1:]
# prevPrice = pricesClose[0]
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
    plt.scatter(points, pricesClose, s=size, alpha=1)
    plt.show()

    rates = []
    rateDates = dates[1:]
    prevPrice = pricesClose[0]
    for price in pricesClose[1:]:
        rate = (price - prevPrice)/price
        prevPrice = price
        rates.append(rate)
    for i in range(len(rateDates)):
        if(abs(rates[i]) > .1):
            print "date:" , rateDates[i] , "price:" , rates[i]
    points = range(len(rateDates))
    size = []
    for i in range(len(rateDates)):
        size.append(.5)
    plt.scatter(points,rates, s=size)
    plt.show()


