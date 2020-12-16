from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

t = np.arange(0, 10, 0.01)
y0 = [0, np.sqrt(2)]

#Solution scipy
def func(y, t):
    return -2 * y
y_sci = odeint(func, y0, t)[:, 1]

#Solution sympy
x = sp.symbols('x')
y = sp.Function('y')
eq = sp.Eq(sp.Derivative(y(x), x), -2 * y(x))
f = sp.dsolve(eq, ics={y(0): sp.sqrt(2)})
y_sym = np.zeros(t.size)
for i in range(t.size):
    y_sym[i] = (f.rhs).subs({x: t[i]}).n()

fig, (graph, dif) = plt.subplots(1, 2,figsize=(15,15))

fig.subplots_adjust(hspace=0.2)
graph.plot(t, y_sci, label='sympy')
graph.plot(t, y_sym, label='scipy')
graph.set(title='Решения дифференциального уравнения')
graph.legend()
graph.grid()

dif.plot(t, y_sym - y_sci)
dif.set_title('Разность решений sympy и scipy')
dif.grid()
plt.show()