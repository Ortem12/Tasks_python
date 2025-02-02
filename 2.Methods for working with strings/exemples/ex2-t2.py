def is_palindrome(word):
    # Сравниваем слово с его обратной версией
    return word == word[::-1]

# Ввод слова от пользователя
word = input("Введите слово: ")

# Проверка, является ли слово палиндромом
result = is_palindrome(word)

# Вывод результата
print(result)