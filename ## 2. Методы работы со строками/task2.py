def is_palindrome(s):
    # Удаляем все небуквенные и нечисловые символы и приводим к нижнему регистру
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Проверяем, совпадает ли строка с её обратной версией
    return cleaned_string == cleaned_string[::-1]

# Пример использования
input_string = input("Введите строку для проверки на палиндром: ")
result = is_palindrome(input_string)

if result:
    print("Это палиндром!")
else:
    print("Это не палиндром.")