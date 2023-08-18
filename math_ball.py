import matplotlib.pyplot as plt
import numpy as np

g = 9.81
a = float(input('Angle: '))
v0 = float(input('Velocity: '))

t = (2 * v0 * np.sin(a)) / g

# x = v0 * t * np.cos(a)
# y = (v0 * t * np.sin(a)) - ((g * t ** 2) / 2)
steps = 100

time = np.linspace(0, t, steps)

xs = v0 * np.cos(a) * steps
ys = v0 * np.sin(a) * steps - ((g * steps ** 2) / 2)

plt.plot(xs, ys, label='Траектория падения')
plt.xlabel('Горизонтальная координата')
plt.ylabel('Вертикальная координата')
plt.title('Траектория падения мяча')
plt.legend()
plt.grid(True)
plt.show()
