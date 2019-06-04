import numpy as np

w1 = 0.01 * np.random.randn(1, 3)
b1 = np.zeros((1,3))
w2 = 0.01 * np.random.randn(1, 4)
b2 = np.zeros((1,4))
w3 = 0.01 * np.random.randn(1, 1)

f = lambda x: 1/(1 + np.exp(-1)) #Sigmoid Function

x = np.random.randn(3,1) #3 X 1
h1 = f(np.dot(w1, x) + b1) #4 X 1
h2= f(np.dot(w2, h1) + b2) #4 X 1
out = np.dot(w3, h2) #1 X 1

print(out)
