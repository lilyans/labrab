import matplotlib.pyplot as plt
filename = input("Введите название файла:")
x = []
y = []
f = open(filename)
number = int(f.readline().split()[0])
for line in f:
    q = [float(n) for n in line.split()]
    x.append(q[0])
    y.append(q[1])
    # обработка случая,когда начинает обрабатываться следующий блок данных в том же файле
    number -=1
    if number == 0:
        break

plt.plot(x, y,marker ='o',linestyle=' ',color='black')
kx = (max(x)- min(x))/10
ky = (max(y)- min(y))/10
plt.axis([min(x) - kx, max(x) + kx, min(y)-ky, max(y)+ky])
plt.title("Number of points" + ": " + str(len(x)))
plt.show()