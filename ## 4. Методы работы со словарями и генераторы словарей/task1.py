def group_by_first_letter(strings):
    # Создаём пустой словарь для группировки
    grouped_dict = {}
    
    # Проходим по каждой строке в списке
    for string in strings:
        # Получаем первую букву строки
        first_letter = string[0].upper()  # Приводим к верхнему регистру 
        
        # Если ключа ещё нет в словаре, создаём пустой список
        if first_letter not in grouped_dict:
            grouped_dict[first_letter] = []
        
        # Добавляем строку в список для соответствующей буквы
        grouped_dict[first_letter].append(string)
    
    return grouped_dict

# Пример использования
input_strings = ["apple", "banana", "cherry", "apricot", "blueberry", "avocado", "coconut"]
result = group_by_first_letter(input_strings)

print("Результат группировки:")
print(result)