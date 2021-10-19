import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

u_x = 0
var_x = 1

u_y = 0
var_y = 1

phis = [0, 0.1, 0.5, 0.8, 0.9, 0.98]
phi = phis[0]

x = np.linspace(-5,5,500)
y = np.linspace(-5,5,500)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y
rv = multivariate_normal([u_x, u_y], [[var_x, phi], [phi, var_y]])

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, rv.pdf(pos),cmap='viridis',linewidth=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Value')
ax.set_title('Gauss(0,1) phi=' + str(phi))

# plt.show()
fig.savefig('gauss_2d_' + str(phi) + '.jpg')