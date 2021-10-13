import matplotlib.pyplot as plt
import numpy as np
import math

# 100 linearly spaced numbers
x = np.arange(-1, 2, 0.01)

# the function, which is y = x^2 here
def y(x):
    if x<0:
        return 0
    elif 0<x<1:
        return -pow(x,4)+2*x*x
    else:
        return 1

plt.plot(x, list(map(y,x)), 'blue')

plt.title('4.18')
plt.xlabel('x')
plt.ylabel('F_X(x)')
# show the plot
plt.show()