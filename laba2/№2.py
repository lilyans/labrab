import numpy as np
import matplotlib.pyplot as plt



arr = np.loadtxt('signal01.dat')
A=[]
for i in range(arr.size):
    if i<9:
        A.append((sum(arr[:i+1]) / (i+1)))
    else:
        A.append((sum(arr[i-9:i]) / 10))
A = np.array(A)
# Визуализация
fig = plt.figure(frameon=True)
graph_1 = fig.add_subplot(1, 2, 1)
graph_2 = fig.add_subplot(1, 2, 2)
graph_1.plot(arr)
graph_2.plot(A)
graph_1.grid(axis='both')
graph_2.grid(axis='both')
graph_1.set(title="До обработки",
            ylim=[0,35],
            xlim=[0,99])
graph_2.set(title="После обработки",
            ylim=[0,35],
            xlim=[0,99])
plt.subplots_adjust(hspace=0.35, wspace = 0.2)
plt.show()