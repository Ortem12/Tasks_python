import re

# Получаем строку от пользователя
input_string = input("Введите строку: ")

# Регулярное выражение для поиска слов с дефисом
r = r'\b\w+-\w+\b'

# Ищем все совпадения
matches = re.findall(r, input_string)

# Выводим результат
print("Слова с дефисом:", matches)