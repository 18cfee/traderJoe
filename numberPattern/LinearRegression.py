# example of training a final regression model
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
# generate regression dataset
X, y = make_regression(n_samples=100, n_features=2, noise=0.1)
# print (X)
# print (y)
# fit final model
model = LinearRegression()
model.fit(X, y)
# define one new data instance
Xnew = [[-1.07296862, -0.52817175]]
# make a prediction
ynew = model.predict(Xnew)
# show the inputs and predicted outputs
print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))

X = [[105,2],[-2343,4],[4234234,5],[-5,6],[-6,7]]
y = [0,.1,.2,.3,.4]
model = LinearRegression()
model.fit(X,y)

Xnew = [[2.2,4]]
ynew = model.predict(Xnew)
print(ynew[0])