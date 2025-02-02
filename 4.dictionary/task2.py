def count_char_freq(text):
    # Создаём пустой словарь для подсчёта частоты символов
    char_freq = {}
    
    # Проходим по каждому символу в строке
    for char in text:
        # Если символ уже есть в словаре, увеличиваем счётчик
        if char in char_freq:
            char_freq[char] += 1
        # Иначе добавляем символ в словарь с начальным значением 1
        else:
            char_freq[char] = 1
    
    return char_freq

# Пример использования
input_text = input("Введите строку: ")
result = count_char_freq(input_text)

print("Частота символов:")
print(result)