# @x1aotian
import matplotlib.pyplot as plt
import numpy as np
from random import choice, seed

seed(1)
pool = [1,2,3,4,5,6,7,8,9]
X = [choice(pool) for i in range(200)]
Y = [choice(pool) for i in range(200)]
Z = [X[i]+Y[i] for i in range(200)]
W = [X[i]*Y[i] for i in range(200)]
V = [X[i]/Y[i] for i in range(200)]

n_= pool
x_ = [X.count(i)/200 for i in pool]
y_ = [Y.count(i)/200 for i in pool]

fig, axs = plt.subplots(2,3,figsize=(14,8))
fig.suptitle('3.85 Relative Frequency')

axs[0,0].set(xlabel='(a) X_value', ylabel='X_frequency')
axs[0,0].hist(X, 9)
axs[0,1].set(xlabel='(a) Y_value', ylabel='Y_frequency')
axs[0,1].hist(Y, 9)

axs[0,2].set(xlabel='(b) Z_value', ylabel='Z_frequency')
axs[0,2].hist(Z, 17)

axs[1,0].set(xlabel='(c) W_value', ylabel='W_frequency')
axs[1,0].hist(W, 18)

axs[1,1].set(xlabel='(d) V_value', ylabel='V_frequency')
axs[1,1].hist(V, 18)

plt.show()
