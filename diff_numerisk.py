import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 - np.power(x, 2)

def exact(t):
    return (np.exp(2 * t) - 1) / (np.exp(2 * t) + 1)

X_0 = 0
T_START = 0
T_END = 3
N_STEPS = 10
STEP_SIZE = (T_END - T_START) / N_STEPS
FINE_RES = 100

t_values = np.linspace(T_START, T_END, N_STEPS)
x_values = np.zeros(N_STEPS)
x_values[0] = X_0

for n in range(0, N_STEPS - 1):
    x_values[n + 1] = x_values[n] + STEP_SIZE * f(x_values[n])

fig_1, ax_1 = plt.subplots()
ax_1.plot(t_values, x_values, label='euler explicit')

FINE_RES = 100
fine_t = np.linspace(T_START, T_END, FINE_RES)
ax_1.plot(fine_t, exact(fine_t), label='exact solution')
ax_1.legend()

x_values_heun = np.zeros(N_STEPS)
x_values_heun[0] = X_0

for n in range(0, N_STEPS - 1):
    x_values_heun[n + 1] = x_values_heun[n] + STEP_SIZE * 0.5 * (f(x_values_heun[n]) + f(x_values_heun[n] + STEP_SIZE * f(x_values_heun[n])))

fig_2, ax_2 = plt.subplots()
ax_2.plot(t_values, x_values_heun, label='heuns method')

fine_t = np.linspace(T_START, T_END, FINE_RES)
ax_2.plot(fine_t, exact(fine_t), label='exact solution')
ax_2.legend()

x_values_RK = np.zeros(N_STEPS)
x_values_RK[0] = X_0

for n in range(0, N_STEPS - 1):
    k_1 = STEP_SIZE * f(x_values_RK[n])
    k_2 = STEP_SIZE * f(x_values_RK[n] + k_1 * 0.5)
    k_3 = STEP_SIZE * f(x_values_RK[n] + k_2 * 0.5)
    k_4 = STEP_SIZE * f(x_values_RK[n] + k_3)

    x_values_RK[n + 1] = x_values_RK[n] + k_1 / 6 + k_2 / 3 + k_3 / 3 + k_4 / 6

fig_3, ax_3 = plt.subplots()
ax_3.plot(t_values, x_values_RK, label='RK4')

fine_t = np.linspace(T_START, T_END, FINE_RES)
ax_3.plot(fine_t, exact(fine_t), label='exact solution')
ax_3.legend()
plt.show()