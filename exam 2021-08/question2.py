import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate


# Part A
data = np.loadtxt('measurements.txt')
t_measurements = data[:, 0]
y_measurements = data[:, 1]

plt.plot(t_measurements, t_measurements, 'b')
plt.plot(t_measurements, y_measurements, 'r')
plt.plot(t_measurements, t_measurements**2, 'g')


# Part B
f = scipy.interpolate.interp1d(t_measurements, y_measurements)
time_steps = np.linspace(0, 1, num=1000, endpoint=True)
y = f(time_steps)
#plt.plot(t, y, 'o', time_steps, f(time_steps), '-')
plt.show()

# Part C
n = 1000
best_error, c_best = 1, 1
for c in np.linspace(1, 2, 11):
    z = time_steps**c
    error = np.linalg.norm(z - y)/(n-1)
    print(f'{c:.2f}->{error}')
    if error < best_error:
        best_error, c_best = error, c

print(f'Lowest error obtained with c={c_best}')
plt.plot(t_measurements, y_measurements, 'r')
plt.plot(time_steps, time_steps**c_best, 'k')
plt.show()


