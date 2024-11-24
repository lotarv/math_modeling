import numpy as np
import matplotlib.pyplot as plt
from math import log, exp, sqrt, cos, sin, pi

# Генерация случайных чисел
def generate_random_sequence(size, seed=0.123, a=36261, m=312500):
    sequence = []
    current = seed
    for _ in range(size):
        current = (a * current) % m
        sequence.append(current / m)
    return sequence

# Распределения
def uniform_distribution(r, a, b):
    return a + r * (b - a)

def exponential_distribution(r, lambd):
    return -log(r) / lambd

def normal_distribution(r1, r2, mu, sigma):
    z1 = mu + sigma * sqrt(-2 * log(r1)) * cos(2 * pi * r2)
    z2 = mu + sigma * sqrt(-2 * log(r1)) * sin(2 * pi * r2)
    return z1, z2

# Статистика
def mean(values):
    return np.mean(values)

def variance(values):
    return np.var(values, ddof=1)

# Параметры распределений
params = {
    "uniform": {"a": 5, "b": 12},
    "exponential": {"lambd": 3},
    "normal": {"mu": 2, "sigma": 2}
}

# Размер выборок
sample_sizes = [10, 20, 50, 100, 1000]

# Сгенерировать данные
random_values = generate_random_sequence(max(sample_sizes))
uniform_data = [uniform_distribution(r, **params["uniform"]) for r in random_values]
exponential_data = [exponential_distribution(r, **params["exponential"]) for r in random_values]
normal_data = []
for i in range(0, len(random_values) - 1, 2):
    normal_data.extend(normal_distribution(random_values[i], random_values[i + 1], **params["normal"]))

# Функция для построения гистограммы и теоретической плотности
def plot_distribution(data, density_func, title, x_range, sample_sizes, ax):
    colors = ["lightblue", "lightgreen", "lightcoral", "gold", "pink"]
    for i, size in enumerate(sample_sizes):
        sample = data[:size]
        ax[i].hist(sample, bins=10, density=True, color=colors[i], alpha=0.7)
        x = np.linspace(*x_range, 100)
        ax[i].plot(x, [density_func(val) for val in x], color="black", lw=1.5)
        ax[i].set_title(f"{title}, N={size}")

# Построить графики
fig, axes = plt.subplots(3, len(sample_sizes), figsize=(15, 10))
fig.suptitle("Распределения и их свойства", fontsize=16)

# Параметры для плотностей
uniform_density = lambda x: 1 / (params["uniform"]["b"] - params["uniform"]["a"]) if params["uniform"]["a"] <= x <= params["uniform"]["b"] else 0
exponential_density = lambda x: params["exponential"]["lambd"] * exp(-params["exponential"]["lambd"] * x) if x >= 0 else 0
normal_density = lambda x: exp(-0.5 * ((x - params["normal"]["mu"]) / params["normal"]["sigma"]) ** 2) / (params["normal"]["sigma"] * sqrt(2 * pi))

plot_distribution(uniform_data, uniform_density, "Равномерное распределение", 
                  (params["uniform"]["a"], params["uniform"]["b"]), sample_sizes, axes[0])

plot_distribution(exponential_data, exponential_density, "Экспоненциальное распределение", 
                  (0, max(exponential_data)), sample_sizes, axes[1])

plot_distribution(normal_data, normal_density, "Нормальное распределение", 
                  (min(normal_data), max(normal_data)), sample_sizes, axes[2])

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# Зависимость статистик от размера выборки
fig, ax = plt.subplots(2, 3, figsize=(15, 8))
titles = ["Равномерное", "Экспоненциальное", "Нормальное"]
datasets = [uniform_data, exponential_data, normal_data]
metrics = [mean, variance]

for i, (title, data) in enumerate(zip(titles, datasets)):
    for j, metric in enumerate(metrics):
        values = [metric(data[:size]) for size in sample_sizes]
        ax[j, i].bar(sample_sizes, values, color="skyblue")
        ax[j, i].set_title(f"{title} - {'Мат. ожидание' if j == 0 else 'Дисперсия'}")
        ax[j, i].set_xticks(sample_sizes)

plt.tight_layout()
plt.show()
