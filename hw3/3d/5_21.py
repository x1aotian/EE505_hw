from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,8,900)
y = np.linspace(-1,8,900)

X, Y = np.meshgrid(x, y)

Z = np.zeros_like(X)

condition = np.logical_and(X > 1, Y > 1)
Z[condition] = 1 - 1 / (X[condition]*X[condition]*Y[condition]*Y[condition])

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('F_x,y')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('5_21')

# plt.show()
fig.savefig('5_21.jpg')