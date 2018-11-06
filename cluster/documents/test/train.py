from sklearn.datasets import load_svmlight_file


def get_data():
    data = load_svmlight_file("housing_scale.txt")
    return data[0], data[1]

train,label = get_data()

import numpy as np
train = train.toarray()

from sklearn.model_selection import train_test_split
x_train,x_val,y_train,y_val = train_test_split(train,label.reshape(506,1))

W = np.array([1]*13).reshape(13,1)
print(W.shape)
b=0

def loss1(y,linear_y):
    return 0.5 * (np.sum(np.power(y - linear_y,2)))/y.shape[0]

# 用于验证对错
def loss2(y,linear_y):
    return 0.5 * np.sum(np.dot((y - linear_y).T,(y-linear_y)))/y.shape[0]

y_pre = b+np.dot(x_train,W)

loss_train = loss1(y_train,y_pre)
print("train_loss:")
print(loss_train)
loss_train = loss2(y_train,y_pre)
print(loss_train)

# 闭式解
x = np.dot(x_train.T,x_train)
x = np.matrix(x).I
W_theta = np.dot(np.dot(x,x_train.T),y_train)
print(W_theta)

y_pre = b+np.dot(x_val,W_theta)
loss_train = loss1(y_val,y_pre)
print(loss_train)

def GradientDescent(maxiter,x,y,theta,alpha):
    xTrains = x.transpose()
    for i in range(0,maxiter):
        hypothesis = np.dot(x,theta)
        loss = (hypothesis-y)
        m = x.shape[0]
        gradient = np.dot(xTrains,loss)/m
        theta = theta - alpha * gradient
        cost = (1.0/(2*m))*np.sum(np.square(np.dot(x,np.transpose(theta.T))-y))
#         print ("cost: %f"%cost)
    return theta


result = []
for i in range(8):
    W_theta = GradientDescent(10, x_val, y_val, W_theta, 0.5)
    y_pre = b + np.dot(x_val, W_theta)
    loss_train = loss1(y_val, y_pre)
    result.append(loss_train)
    print(loss_train)
