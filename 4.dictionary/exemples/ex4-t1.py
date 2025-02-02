# Получаем две строки от пользователя
string1 = input("Введите первую строку (слова, разделённые пробелами): ")
string2 = input("Введите вторую строку (числа, разделённые пробелами): ")

# Разделяем строки на списки
words = string1.split()
numbers = list(map(int, string2.split()))

# Проверяем, что количество слов и чисел совпадает
if len(words) != len(numbers):
    print("Ошибка: количество слов и чисел должно быть одинаковым.")
else:
    # Формируем словарь
    result_dict = dict(zip(words, numbers))
    print("Результат:", result_dict)
    