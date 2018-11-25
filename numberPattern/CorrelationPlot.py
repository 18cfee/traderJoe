import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    file = open("0-9Pattern0,2,4,6,8Ans","r")
    trainingData = []
    answerData = []
    for i in range(10):
        trainingData.append([])

    a = 0
    for line in file:
        line = line.strip('\n')
        list = line.split(" ")
        i = 0
        if a < 4:
            for num in list:
                trainingData[i].append(num)
                i = i + 1
        else:
            for num in list:
                answerData.append(num)
        a = a + 1

    for entry in trainingData:
        print(entry)

    file.close()

    np.random.seed(19680801)

    N = 50
    x = range(N)
    for item in x:
        x[item] = item*2
    y = range(N)
    x[30] = 17
    print("co",np.corrcoef(x,y)[0][1])
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()
    #
    # plt.scatter(x, y, s=area, c=colors, alpha=0.8)
    # plt.show()

    predict = [2,3,4,4]

