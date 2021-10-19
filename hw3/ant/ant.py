import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from random import uniform

times = 100
# prob = 0.5
prob = 0.6
step = 5

hori = True
x = [50]
y = [50]

for i in range(times):
    p = uniform(0,1)
    if hori:
        if p <= prob:
            x.append(x[i] + step)
        else:
            x.append(x[i] - step)
        y.append(y[i])
    else:
        if p <= prob:
            y.append(y[i] + step)
        else:
            y.append(y[i] - step)
        x.append(x[i])
    hori = not hori

fig = plt.figure()
plt.xlim(-50, 150)
plt.ylim(-50, 150)

graph, = plt.plot([], [], color = 'b', marker='o', markersize=6)
graph1, = plt.plot([], [], 'b.')
plt.plot(50, 50, color = 'r', marker='^', markersize=10)


def animate(i):
    graph.set_data(x[i], y[i])
    graph1.set_data(x[max(0,i-10):i], y[max(0,i-10):i])
    return graph


anim = FuncAnimation(fig, animate, interval=200, frames=times+1)


writergif = PillowWriter(fps=30)
anim.save('prob_' + str(prob) + '.gif', writer=writergif)