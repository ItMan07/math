import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 16, 8, 4, 7]

plt.scatter(x, y, color='red', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()
