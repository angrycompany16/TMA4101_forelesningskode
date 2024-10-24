import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-np.power(x, 2))

N = 10 # number of steps
A = 0
B = 1

# integrate f(x) from A to B
s_left = 0
for k in range(N):
    s_left += (B - A) / N * f(A + (B - A) / N * k)

print(s_left)

# plotting
x_values = np.linspace(A - 1, B + 1, 100)
y_values = f(x_values)
fig_1, ax_1 = plt.subplots()
ax_1.plot(x_values, y_values)

grid_steps = [A + (B - A) / N * k for k in range(N)]
bar_heights = [f(x) for x in grid_steps]
ax_1.bar(grid_steps, bar_heights, width=((B - A) / N), alpha=0.2, align='edge', edgecolor='b')

# integrate f(x) from A to B
s_trap = 0
for k in range(N):
    s_trap += (B - A) / N * (f(A + (B - A) / N * k) + f(A + (B - A) / N * (k + 1))) / 2

print(s_trap)

# plotting
fig_2, ax_2 = plt.subplots()
ax_2.plot(x_values, y_values)

for k in range(N):
    x = A + (B - A) / N * k
    x_next = A + (B - A) / N * (k + 1)

    y = f(x)
    y_next = f(x_next)

    ax_2.fill([x, x, x_next, x_next], [0, y, y_next, 0], 'b', edgecolor='b', alpha=0.2)


H = (B - A) / N

# integrate f(x) from A to B
s_simp = 0
for k in range(N):
    x = A + H * k
    x_next = A + H * (k + 1)

    s_simp += (x_next - x) / 6 * (f(x) + 4 * f((x_next + x) / 2) + f(x_next))

print(s_simp)

EX = 0.7468241328124270253994674361318530053544996868126063290276544989

print("------------------------------------")
print("Sammenligning i feil:")
print("------------------------------------")
print(f'Venstre Riemann: {abs(EX - s_left)}')
print(f'Trapesmetoden: {abs(EX - s_trap)}')
print(f'Simpsons metode: {abs(EX - s_simp)}')

plt.show()
