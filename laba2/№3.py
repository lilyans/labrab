import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.loadtxt('start.dat')
k = data.shape[0]# размер строки
number = 60
arr = np.loadtxt('start.dat').reshape(k,1) # перевод строки в столбец
A = np.fromfunction(lambda x, y: x == (y+1), (k, k), dtype=int)*(-1)+np.eye(k) + np.fromfunction(lambda x,y: ((x == 0) & (y == k -1)), (k, k), dtype=int)*(-1)
q = []
for m in range(number):
    q.append(arr)
    arr = arr + (-0.5)*A.dot(arr)

# Визуализация
fig, ax = plt.subplots()
def animate(i):
    ax.clear()
    el = q[i].reshape(1, k).tolist()[0]
    ax.axis([0,k,0,max(a.max() for a in q)])
    ax.grid(axis="both")
    line = ax.plot(el)
    return line
lab_animation = animation.FuncAnimation(fig,
                                      animate,
                                      frames=number,
                                      interval = 0,
                                      repeat = True)
lab_animation.save('lab_numpy.gif',fps=20)