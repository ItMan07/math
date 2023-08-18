import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [15, 24, 12, 32]

plt.bar(categories, values, color='green')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()
