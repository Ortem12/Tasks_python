def unique_sorted_words(text):
    # Разделяем строку на слова, приводим их к верхнему регистру и удаляем дубликаты
    unique_words = set(word.upper() for word in text.split())
    
    # Сортируем слова по алфавиту
    sorted_words = sorted(unique_words)
    
    return sorted_words

# Пользователь вводит строку
user_input = input("Введите строку из 2 или более слов: ")

# Вызов функции и получение результата
result = unique_sorted_words(user_input)

# Вывод результата
print("Отсортированный список уникальных слов в верхнем регистре:")
print(result)