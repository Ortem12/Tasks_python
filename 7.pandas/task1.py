import pandas as pd

# Входные данные
students_data = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 78},
    {"name": "Charlie", "age": 19, "grade": 92},
    {"name": "Diana", "age": 21, "grade": 74},
    {"name": "Eve", "age": 20, "grade": 88},
    {"name": "Frank", "age": 23, "grade": 81},
    {"name": "Grace", "age": 18, "grade": 95},
    {"name": "Hank", "age": 22, "grade": 67},
    {"name": "Ivy", "age": 19, "grade": 90},
    {"name": "Jack", "age": 21, "grade": 76},
    {"name": "Kara", "age": 20, "grade": 83},
    {"name": "Leo", "age": 24, "grade": 72},
    {"name": "Mona", "age": 19, "grade": 86},
    {"name": "Nate", "age": 22, "grade": 65},
    {"name": "Olivia", "age": 18, "grade": 93},
    {"name": "Paul", "age": 21, "grade": 88},
    {"name": "Quinn", "age": 23, "grade": 79},
    {"name": "Rose", "age": 20, "grade": 84},
    {"name": "Sam", "age": 19, "grade": 91},
    {"name": "Tina", "age": 21, "grade": 75},
    {"name": "Uma", "age": 20, "grade": 80},
    {"name": "Victor", "age": 23, "grade": 77},
    {"name": "Wendy", "age": 22, "grade": 82},
    {"name": "Xander", "age": 19, "grade": 89},
    {"name": "Yara", "age": 18, "grade": 94},
    {"name": "Zack", "age": 21, "grade": 73}
]

# Создаём DataFrame
df = pd.DataFrame(students_data)

# Фильтруем студентов с оценкой выше 80
filtered_df = df[df['grade'] > 80]

# Сортируем по имени в алфавитном порядке
sorted_df = filtered_df.sort_values(by='name')

# Сохраняем результат в CSV-файл
sorted_df.to_csv('filtered_students.csv', index=False)

print("Результат сохранён в файл 'filtered_students.csv'")