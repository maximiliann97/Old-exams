from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np


def derivative(y, t, beta, gamma, mu, N):
    S, I, R, D = y
    dS_dt = -beta * I * S / N
    dI_dt = beta * I * S / N - gamma * I - mu * I
    dR_dt = gamma * I
    dD_dt = mu * I

    dy_dt = [dS_dt, dI_dt, dR_dt, dD_dt]
    return dy_dt


N = 1e7
gamma = 1 / 7
mu = 0.001 * gamma
R = 1.5
beta = gamma * R

y_t0 = [N, 10, 0, 0]
t = np.linspace(1, 365, 365)

sol = odeint(derivative, y_t0, t, args=(beta, gamma, mu, N))

plt.plot(t, sol[:, 0], 'b', label='S, Susceptible')
plt.plot(t, sol[:, 1], 'g', label='I')
plt.plot(t, sol[:, 2], 'r', label='R, Recovered')
plt.plot(t, sol[:, 3], 'y', label='D')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

