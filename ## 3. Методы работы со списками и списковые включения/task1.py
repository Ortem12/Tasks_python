def process_numbers(numbers):
    # Удаляем отрицательные числа
    positive_numbers = [num for num in numbers if num >= 0]
    
    # Сортируем числа по убыванию
    sorted_numbers = sorted(positive_numbers, reverse=True)
    
    return sorted_numbers

# Пример использования
input_numbers = [3, -1, 7, -5, 2, 10, -8, 15, 0, 4, -3, 12, -9, 6, 1, -2, 8, -4, 11, -7]
result = process_numbers(input_numbers)

print("Результат обработки списка:")
print(result)