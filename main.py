import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)

x = np.linspace(-10, 10, 100)
y = x ** 2

plt.plot(x, y, label='y=x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = x ^ 2')
plt.legend()
plt.grid()
plt.show()

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()
