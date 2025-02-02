import numpy as np

# Генерация массива 10x10 со случайными числами от 1.01 до 9.99
array = np.random.uniform(1.01, 9.99, (10, 10))

# Вывод массива
print("Сгенерированный массив:")
print(array)

# Вывод главной диагонали
diagonal = np.diag(array)
print("\nГлавная диагональ:")
print(diagonal)

# Вычисление и вывод статистических данных
mean_value = np.mean(array)
min_value = np.min(array)
max_value = np.max(array)
median_value = np.median(array)
variance_value = np.var(array)
std_deviation_value = np.std(array)

print("\nСтатистические данные:")
print(f"Среднее значение: {mean_value:.2f}")
print(f"Минимальный элемент: {min_value:.2f}")
print(f"Максимальный элемент: {max_value:.2f}")
print(f"Медиана: {median_value:.2f}")
print(f"Дисперсия: {variance_value:.2f}")
print(f"Стандартное отклонение: {std_deviation_value:.2f}")