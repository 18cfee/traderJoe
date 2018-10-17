print ("working")

x = 5
x += 1
print (x)



def myMethod():
    print("method call")
    y = x + 1
    x = y
    print(x)


if __name__ == '__main__':
    myMethod()