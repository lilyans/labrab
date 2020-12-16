def get_ax_limits(q):  # Находим общие пределы для осей
    Mx_x = []
    Mn_x = []
    Mx_y = []
    Mn_y = []
    for i in range(len(q)):
        if i % 2 == 0:
            Mx_x.append(max(q[i]))
            Mn_x.append(min(q[i]))
        else:
            Mx_y.append(max(q[i]))
            Mn_y.append(min(q[i]))
    return [min(Mn_x), max(Mx_x), min(Mn_y) - 1, max(Mx_y) + 1]


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation

filename = input("Введите название файла:")
f = open(filename)
q = []
for line in f:
    q.append([float(n) for n in line.split()])

# Визуализация в виде большого графика
fig = plt.figure(figsize=[6, 30])
for i in range(1, int(len(q) / 2) + 1):
    graph = fig.add_subplot(3, 2, i)
    graph.plot(q[i * 2 - 2], q[i * 2 - 1])
    graph.set(
        title="Frame" + " " + str(i),
        xlim=[get_ax_limits(q)[0], get_ax_limits(q)[1]],
        ylim=[get_ax_limits(q)[2], get_ax_limits(q)[3]])
    graph.grid(axis='both')
    graph.xaxis.set_major_locator(ticker.MultipleLocator(3))  # деления сетки по х
    graph.yaxis.set_major_locator(ticker.MultipleLocator(3))  # деления сетки по у

plt.subplots_adjust(hspace=0.35, wspace=0.2)
plt.show()

# Визуализация в виде gif-файла(lab.gif)
fig, ax = plt.subplots()


def animate(i):
    ax.clear()
    ax.axis(get_ax_limits(q))
    line = ax.plot(q[i * 2 - 2], q[i * 2 - 1])
    return line


lab_animation = animation.FuncAnimation(fig,
                                        animate,
                                        frames=6,
                                        interval=10,
                                        repeat=True)
lab_animation.save('lab.gif', fps=10)