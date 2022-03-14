import numpy as np
import scipy
import matplotlib.pyplot as plt

# Part A
data = np.loadtxt('values.txt')
x = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]
ys = [y1, y2]
# Part B
fig, ax = plt.subplots()
ax.plot(x, y1, 'r.')
ax.plot(x, y2, 'b.')


def polynomial_1(x, A, B):
    return A + B*x


def polynomial_2(x, A, B, C):
    return A + B*x + C*x**2
counter = 0
for y in ys:
    poly1_set1 = np.polyfit(x, y, deg=1)
    poly2_set1 = np.polyfit(x, y, deg=2)
    A = [poly1_set1[0], poly2_set1[0]]
    B = [poly1_set1[1], poly2_set1[1]]
    C = poly2_set1[2]
    if counter == 0:
        ax.plot(x, polynomial_1(x, A[0], B[0]), 'g.')
        ax.plot(x, polynomial_2(x, A[1], B[1], C), 'k.')
    else:
        ax.plot(x, polynomial_1(x, A[0], B[0]), 'm.')
        ax.plot(x, polynomial_2(x, A[1], B[1], C), 'c.')

    counter += 1
leg_labels = ['y1', 'y2', 'Polynomial order 1 (y1)', 'Polynomial order 2 (y1)', 'Polynomial order 1 (y2)',
              'Polynomial order 2 (y2)']
plt.title('Polynomials')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(leg_labels)

plt.show()