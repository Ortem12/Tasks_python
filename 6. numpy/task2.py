import numpy as np

# Параметры временного ряда
length = 10000  # Длина временного ряда
amplitude = 10  # Амплитуда синусоиды (колебания температуры)
noise_amplitude = 5  # Амплитуда случайного шума

# Генерация временного ряда
time = np.arange(length)  # Ось времени (дни)
temperature = amplitude * np.sin(2 * np.pi * time / 365) + np.random.uniform(-noise_amplitude, noise_amplitude, length)

# 1. Среднее и стандартное отклонение
mean_temp = np.mean(temperature)
std_temp = np.std(temperature)

# 2. Минимальная и максимальная температура, а также их индексы
min_temp = np.min(temperature)
max_temp = np.max(temperature)
min_index = np.argmin(temperature)
max_index = np.argmax(temperature)

# 3. Количество дней подряд, когда температура была ниже среднего
below_mean = temperature < mean_temp
streaks = np.diff(np.where(np.concatenate(([below_mean[0]], below_mean[:-1] != below_mean[1:], [True])))[0])[::2]
max_streak = np.max(streaks) if streaks.size > 0 else 0

# Вывод результатов
print(f"Средняя температура за весь период: {mean_temp:.2f}°C")
print(f"Стандартное отклонение температуры: {std_temp:.2f}°C")
print(f"Минимальная температура: {min_temp:.2f}°C (день {min_index})")
print(f"Максимальная температура: {max_temp:.2f}°C (день {max_index})")
print(f"Максимальное количество дней подряд с температурой ниже среднего: {max_streak}")