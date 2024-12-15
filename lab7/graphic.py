import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 15, 400)

# Граничные прямые
y1 = (2 / 5) * x1 + 2
y2 = -4 / 5 * x1 + 8
y3 = -1 / 5 * x1 + 1

plt.figure(figsize=(10, 8))

# Графики ограничений
plt.plot(x1, y1, label=r"$2x_1 - 5x_2 \geq -10$", color='blue')
plt.plot(x1, y2, label=r"$4x_1 + 5x_2 \leq 40$", color='green')
plt.plot(x1, y3, label=r"$x_1 + 5x_2 \geq 5$", color='red')

# Заполнение допустимой области
plt.fill_between(x1, np.maximum(0, y3), np.minimum(y1, y2), where=(np.minimum(y1, y2) >= np.maximum(0, y3)), 
                 color='gray', alpha=0.3, label="ОДР")

# Линейная форма z(x) = x1 + 2x2 -> max/min
z = (lambda x1: (10 - x1) / 2)
plt.plot(x1, z(x1), label=r"gradF", linestyle='--', color='orange')

# Построение стрелки от (0,0) до (1,2) и её продление
start_x, start_y = 0, 0
end_x, end_y = 1.2, 4.8  # Увеличиваем длину стрелки
plt.arrow(start_x, start_y, end_x - start_x, end_y - start_y, 
          head_width=0.3, head_length=0.3, fc='purple', ec='purple', linewidth=2)

# Выделение точки (5,4) жирным
plt.scatter(5, 4, color='black', s=100, label="Точка (5,4)", edgecolor='yellow', linewidth=2)
plt.scatter(0, 1, color='black', s=100, label="Точка (0,1)", edgecolor='yellow', linewidth=2)


# Настройки графика
plt.xlim(-5, 20)
plt.ylim(-5, 20)

plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")
plt.title("Решение задачи линейного программирования графическим методом")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.show()
