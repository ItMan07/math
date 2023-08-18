import matplotlib.pyplot as plt
import numpy as np

# Параметры
initial_velocity = float(input("Введите начальную скорость (м/с): "))
angle_degrees = float(input("Введите угол броска (градусы): "))
angle_radians = np.radians(angle_degrees)
gravity = 9.81  # Ускорение свободного падения (м/с^2)

# Рассчет траектории
time_of_flight = (2 * initial_velocity * np.sin(angle_radians)) / gravity
time_intervals = np.linspace(0, time_of_flight, num=100)
x_positions = initial_velocity * np.cos(angle_radians) * time_intervals
y_positions = initial_velocity * np.sin(angle_radians) * time_intervals - (0.5 * gravity * time_intervals**2)

# Построение графика
plt.plot(x_positions, y_positions, color='blue', label='Траектория падения')
plt.xlabel('Горизонтальное расстояние (м)')
plt.ylabel('Вертикальное расстояние (м)')
plt.title('Траектория падения мяча')
plt.legend()
plt.grid(True)
plt.show()
