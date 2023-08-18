import matplotlib.pyplot as plt

# Создаем пустой список для хранения введенных значений
x_values = []
y_values = []

plt.xlabel('x')
plt.ylabel('y')
plt.title('График с динамическим обновлением')
print('Для завершения ввода введите q')

while True:
    try:
        x = input("x: ")
        if x == 'q':
            break
        x = float(x)
        y = float(input("y: "))

        x_values.append(x)
        y_values.append(y)

        plt.clf()  # Очищаем предыдущий график
        plt.plot(x_values, y_values, marker='o', color='blue')
        plt.grid(True)
        plt.pause(0.1)  # Пауза для обновления графика

    except ValueError:
        print("Некорректный ввод. Введите числа или 'q' для завершения.")

plt.show()  # показать окончательный график
