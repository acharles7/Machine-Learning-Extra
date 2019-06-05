import numpy as np

x = np.random.randn()

h = np.tanh(np.dot(W_hh, h) + np.dot(W_xh, x))
y = np.dot(W_hy, h)

return y
