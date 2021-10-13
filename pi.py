# @x1aotian
import random as rd
import numpy as np

ns = [pow(10,i) for i in range(2,9)]
pis = []

for n in ns:
    xs = np.random.uniform(low=-1, high=1, size=(n,))
    ys = np.random.uniform(low=-1, high=1, size=(n,))
    in_ = 0
    for i in range(n):
        if pow(xs[i],2) + pow(ys[i],2) <= 1:
            in_ += 1
    pis.append(4 * in_ / n)

print("num_nodes | pi" )
for i in range(len(ns)):
    print("{:9} | {:.8f}".format(ns[i], pis[i]))
        
