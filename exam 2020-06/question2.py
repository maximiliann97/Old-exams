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

deaths_per_day = np.diff(sol[:, 3])

# print(len(deaths_per_day))  # length is 364 for some weird reason?
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(t, sol[:, 0], 'b', label='S, Susceptible')
axs[0, 0].plot(t, sol[:, 2], 'r', label='R, Recovered')
axs[0, 0].set_xlabel('Time (days)')
axs[0, 0].set_ylabel('S susceptible, R recovered\n(million people)')
axs[0, 0].legend(loc='best')

axs[1, 0].plot(t, sol[:, 1], 'g', label='I')
axs[1, 0].set_xlabel('Time (days)')
axs[1, 0].set_ylabel('I Infectious (people)')

axs[0, 1].plot(t, sol[:, 3], 'y', label='D')
axs[0, 1].set_xlabel('Time (days)')
axs[0, 1].set_ylabel('D deceased (people)')

t = np.linspace(1, 364, 364)
axs[1, 1].plot(t, deaths_per_day)
axs[1, 1].set_xlabel('Time (days)')
axs[1, 1].set_ylabel('Daily number of deceased\n(people per day)')
plt.grid()
plt.show()


