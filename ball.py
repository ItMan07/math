import matplotlib.pyplot as plt
import numpy as np

# Константы
g = 9.81  # Ускорение свободного падения
angle_deg = 45  # Угол броска в градусах
angle_rad = np.radians(angle_deg)  # Перевод угла в радианы

# Время
time_of_flight = 2 * np.sqrt(2 * 10 / g)  # Время полета
time_steps = 100  # Количество шагов во времени
time = np.linspace(0, time_of_flight, time_steps)  # Массив временных шагов

# Рассчет координат
x = (10 * np.cos(angle_rad)) * time  # Горизонтальная координата
y = (10 * np.sin(angle_rad)) * time - 0.5 * g * time ** 2  # Вертикальная координата

# Построение графика
plt.plot(x, y, color='blue')
plt.xlabel('Горизонтальная координата')
plt.ylabel('Вертикальная координата')
plt.title('Траектория падения мяча под углом 45 градусов')
plt.grid(True)
plt.show()
