# Получаем строку от пользователя
input_string = input("Введите строку чисел, разделённых пробелами: ")

# Преобразуем строку в список целых чисел
numbers = list(map(int, input_string.split()))

# Считаем, сколько раз каждое число встречается в списке
counts = {}
for num in numbers:
    counts[num] = counts.get(num, 0) + 1

# Формируем новый список, исключая числа, которые встречаются только один раз
filtered_numbers = [num for num in numbers if counts[num] > 1]

# Выводим результат без скобок
print("Результат:", *filtered_numbers)