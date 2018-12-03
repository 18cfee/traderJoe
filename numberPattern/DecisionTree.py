from sklearn import tree
if __name__ == '__main__':
    file = open("0-9DoublePattern0,2,4,6,8Ans","r")
    trainingData = []
    answerData = []
    for i in range(10):
        trainingData.append([])

    a = 0
    for line in file:
        line = line.strip('\n')
        list = line.split(" ")
        i = 0
        if a != 3:
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

    clf = tree.DecisionTreeClassifier(max_depth=5)
    clf = clf.fit(trainingData,answerData)
    predict2 = [[2,3,4,4],[8,9,6,-235]]
    print(clf.predict(predict2))
    print(clf.predict(trainingData))

