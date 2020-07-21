import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sympy as syp

y_space = np.linspace(0,1,1000)
#y : concentration of weak acid, x : 해리된 약산의 몰농도

x = syp.symbols("x")
y = syp.symbols("y")
K_a = 1.76e-4
f = K_a*y - K_a*x - x**2
y_equ = syp.solve(f,x)[1]

x_space = np.array([])
for ys in y_space:
    x_space = np.append(x_space,[y_equ.subs(y,ys)])

Kai_space = np.array([])
for i in range(len(x_space)):
    xs = x_space[i]
    ys = y_space[i]
    kais = xs / ys
    Kai_space = np.append(Kai_space,[kais])

plt.plot(y_space, Kai_space)
#plt.ylim(0.9999,1.0001)
print(Kai_space)
plt.show()

