
# coding: utf-8

# In[21]:

from numpy import *

def costFunction(theta0,theta1,data):
    errorRate=0
    for i in range (0,len(data)):
        x=data[i,0]
        y=data[i,1]
        errorRate+=(y-(theta1*x+theta0))**2
    return errorRate/len(data)

def gradientDescentRunner(theta0,theta1,learningRate,data):
    initial_0=0
    initial_1=0
    for i in range (0,len(data)):
        x=data[i,0]
        y=data[i,1]
        initial_0+=-2*(y-(theta1*x+theta0))/len(data)
        initial_1+=-2*x*(y-(theta1*x+theta0))/len(data)
    theta0=theta0-(learningRate*initial_0)
    theta1=theta1-(learningRate*initial_1)
    return[theta0,theta1]

def looper(theta0,theta1,data,iterations,learningRate):
    new_theta0=theta0
    new_theta1=theta1
    for i in range(iterations):
        new_theta0,new_theta1=gradientDescentRunner(new_theta0,new_theta1,learningRate,data)
        print(new_theta0,new_theta1)
    return[new_theta0,new_theta1]

def run():
    data=genfromtxt("data.csv", delimiter=",")
    theta0=0
    theta1=0
    iterations=200
    learningRate=0.0001
    errorVal=costFunction(theta0,theta1,data)
   # print(errorVal)
    [r,y]=looper(theta0,theta1,data,iterations,learningRate)
    #print(r,y)
    #newerrorVal=costFunction(r,y,data)
    #print(newerrorVal)
if __name__ == '__main__':
    run()
    


# In[ ]:




# In[ ]:



