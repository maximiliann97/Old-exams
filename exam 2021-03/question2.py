import numpy as np
import scipy.integrate as integrate
import math
import matplotlib.pyplot as plt


def time_derivative(s: np.array, t: float, params):
    m, g, c = params
    v = s[0:2]
    ev = v / np.linalg.norm(v)
    fw = -c/m * np.linalg.norm(v)**2 * ev
    ds_dt = [fw[0] / m,
             -g + fw[1] / m,
             s[0],
             s[1]
             ]
    return np.array(ds_dt)


def simulate_projectile(ang: float, c: float):
    params = [0.1, 9.82, c]  # m, g, c
    s0 = np.array([10 * math.cos(ang), 10 * math.sin(ang), 0, 0])
    t = np.arange(0, 2, 0.1)
    sol = integrate.odeint(time_derivative, s0, t, args=(params,))
    return sol


alpha = [math.pi/3, math.pi/4, math.pi/5, math.pi/6]
c = [0, 0.001, 0.002]
x = np.linspace(0, 15, num=20)
fig, axs = plt.subplots(2, 2)
axes = [[0, 0], [0, 1], [1, 0], [1, 1]]
angels = ['α = π/3', 'α = π/4', 'α = π/5', 'α = π/6']
index = 0


for a in alpha:
    for i in c:
        sol = simulate_projectile(a, i)
        xs = [d[2] for d in sol]
        ys = [d[3] for d in sol]
        pos = axes[index]
        axs[pos[0], pos[1]].plot(xs, ys)
        axs[pos[0], pos[1]].set_xlim([0, 17])
        axs[pos[0], pos[1]].set_ylim([-9, 6])
        axs[pos[0], pos[1]].set_xlabel('x[m]')
        axs[pos[0], pos[1]].set_ylabel('y[m]')
        axs[pos[0], pos[1]].set_title('{}'.format(angels[index]))
        axs[pos[0], pos[1]].legend(c, title='c')

    index += 1


plt.show()



