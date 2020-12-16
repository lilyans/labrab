import numpy as np
import matplotlib.pyplot as plt

f = open('small.txt')
N = int(f.readline())
arr = np.loadtxt(f)
b = arr[-1]
A = arr[0:-1].reshape(N,N)
y = np.linalg.solve(A,b)
x = np.arange(0,len(y))

fig, ax = plt.subplots()
plt.grid()
ax.bar(x, y,color='darkgreen')
ax.set(xlabel="Номер решения",
       ylabel='X(i)')

fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()