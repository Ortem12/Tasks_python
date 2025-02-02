import numpy as np

# Ввод размеров массива от пользователя
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Создание массива случайных чисел от 1 до 100
array = np.random.randint(1, 101, size=(rows, cols))

# Вычисление суммы элементов каждой строки
row_sums = np.sum(array, axis=1)

# Вывод результата
print("Исходный массив:")
print(array)
print("\nСуммы элементов каждой строки:")
print(row_sums)