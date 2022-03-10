import numpy as np


def time_derivate(s, t, params):
    m, g, c = params
    v = s[0:2]
    ev = -v / np.linalg.norm(v)
    fw = -c * np.linalg.norm(v)**2 * ev
    dsdt = [fw[0] / m,
            -g + fw[1],
            s[0],
            s[1]
            ]
    return np.array(dsdt)




alpha = 10
s = np.array([10*np.cos(alpha), 10*np.sin(alpha), 0, 0])
t = 10
params = [0.1, 9.82, 1]
dsdt = time_derivate(s, t, params)
print(dsdt)