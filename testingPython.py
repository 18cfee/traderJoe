import numpy
from MarketOverView import MarketOverView



def myMethod():
    print("method call")

def numpyZeroes():
    print("two is running",'\n')
    pos=numpy.zeros(1)
    print(pos)
    cond = 2 > 1
    pos[cond]=-1
    print(pos)
    pos[0] = 7
    pos = [1]
    print(pos)

    print(1 == 1)

    state = MarketOverView()

    print("test class", state.isInCrashState())


if __name__ == '__main__':
    myMethod()
    numpyZeroes()