from scipy.optimize import minimize, basinhopping, root
from math import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt


# Part A
def evaluation(x):
    return (x-2)**2 + 15*np.sin(x)

x = np.arange(-10, 10, 0.1)


fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, evaluation(x))
axs[0, 1].plot(x, evaluation(x))
axs[1, 0].plot(x, evaluation(x))
axs[1, 1].plot(x, evaluation(x))

x0 = [1, 5, 7, 10]
for x in x0:
    bfgs = minimize(evaluation, x, method='BFGS')
    cg = minimize(evaluation, x, method='CG')
    powell = minimize(evaluation, x, method='powell')

    print('BFGS finds the local minima: {} with start guess x = {}'.format(bfgs.x, x))
    print('CG finds the local minima: {} with start guess x = {}'.format(cg.x, x))
    print('Powell finds the local minima: {} with start guess x = {}\n'.format(powell.x, x))

    axs[0, 0].plot(bfgs.x, evaluation(bfgs.x), 'ro')
    axs[0, 1].plot(cg.x, evaluation(cg.x), 'ro')
    axs[1, 0].plot(powell.x, evaluation(powell.x), 'ro')

# Part B
res = basinhopping(evaluation, 3)
print('Global minima: {}\n'.format(res.x))

roots = set()
start_guesses = [-15, -7, -2, 1, 2, 3, 4, 6, 7, 9, 10]
# Part C
for x in start_guesses:
    sol = root(evaluation, x)
    int_sol = float(sol.x)
    int_sol = round(int_sol, 6)
    roots.add(int_sol)

roots = list(roots)
roots = np.array(roots)

axs[1, 1].plot(roots, evaluation(roots), 'y*')
axs[1, 1].plot(res.x, evaluation(res.x), 'ro ')
print('Roots are:', roots)

axs[0, 0].legend(['f(x)=(x −a)2+ b sin(x)', 'Local minima'])
axs[0, 1].legend(['f(x)=(x −a)2+ b sin(x)', 'Local minima'])
axs[1, 0].legend(['f(x)=(x −a)2+ b sin(x)', 'Local minima'])
axs[1, 1].legend(['f(x)=(x −a)2+ b sin(x)', 'Roots', 'Global minima'])

axs[0, 0].set_xlim(-10, 10)
axs[0, 1].set_xlim(-10, 10)
axs[1, 0].set_xlim(-10, 10)
axs[1, 1].set_xlim(-10, 10)

axs[0, 0].set_title('Broyden-Fletcher-Goldfarb-Shanno')
axs[0, 1].set_title('Conjugate Gradien')
axs[1, 0].set_title('Powell')
axs[1, 1].set_title('')

axs[0, 0].set_xlabel('x')
axs[0, 1].set_xlabel('x')
axs[1, 0].set_xlabel('x')
axs[1, 1].set_xlabel('x')

axs[0, 0].set_ylabel('y')
axs[0, 1].set_ylabel('y')
axs[1, 0].set_ylabel('y')
axs[1, 1].set_ylabel('y')


plt.show()