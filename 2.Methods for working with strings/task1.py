def count_word_freq(text):
    # Создаём обычный словарь для подсчёта частоты слов
    word_freq = {}
    
    # Приводим текст к нижнему регистру
    text = text.lower()
    
    # Удаляем знаки препинания (простой способ)
    for char in '.,!?;:"\'()':
        text = text.replace(char, ' ')
    
    # Разделяем текст на слова
    words = text.split()
    
    # Подсчитываем частоту каждого слова
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

# Пример текста
text = """
Applications in Data Analysis

NumPy is a foundational tool for data analysis. It integrates seamlessly with libraries like Pandas, Matplotlib, and Scikit-learn. When working with large datasets, preprocessing tasks such as normalization, reshaping, and handling missing data often rely on NumPy’s capabilities. Additionally, its integration with other libraries makes it a core component of the Python data ecosystem.
In conclusion, mastering NumPy arrays is essential for anyone looking to excel in numerical computing or data analysis. Its efficiency, flexibility, and integration with other tools make it an invaluable asset for Python programmers.
"""

# Подсчёт частоты слов
freq = count_word_freq(text)

# Вывод результата
print("Частота слов:")
for word, count in sorted(freq.items()):  # Сортируем слова по алфавиту
    print(f"{word}: {count}")