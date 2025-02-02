import pandas as pd
import random

# Списки имен и фамилий
first_names = ['Ольга', 'Мария', 'Марина', 'София', 'Дмитрий', 'Елена', 'Артем', 'Сергей', 'Александр', 'Александра', 
               'Екатерина', 'Никита', 'Иван', 'Павел', 'Анастасия', 'Юлия', 'Олег', 'Кирилл', 'Алексей', 'Анна']
last_names = ['Егорова', 'Николаева', 'Ефремова', 'Сидорова', 'Смирнов', 'Кузнецов', 'Морозова', 'Петров', 'Иванов', 
              'Николаев', 'Егоров', 'Сидоров', 'Кузнецова', 'Морозов', 'Петрова', 'Иванова']

# Списки для выбора должностей и отделов
positions = ['Разработчик', 'Маркетолог', 'Финансовый аналитик', 'Менеджер']
departments = ['Отдел разработки', 'Отдел продаж', 'Отдел маркетинга', 'Отдел финансов']

# Генерация уникальных комбинаций имен и фамилий
unique_names = set()
while len(unique_names) < 35:
    full_name = (random.choice(first_names), random.choice(last_names))
    unique_names.add(full_name)

# Преобразование множества в список для удобства
unique_names = list(unique_names)

# Генерация данных для DataFrame
data = {
    'Имя': [],
    'Фамилия': [],
    'Отдел': [],
    'Должность': [],
    'Зарплата': []
}

for name, surname in unique_names:
    data['Имя'].append(name)
    data['Фамилия'].append(surname)
    data['Отдел'].append(random.choice(departments))
    data['Должность'].append(random.choice(positions))
    data['Зарплата'].append(random.randint(90000, 300000))

# Создание DataFrame
df = pd.DataFrame(data)

# Вывод DataFrame
print(df)

# Определение минимальной и максимальной зарплаты
min_salary = df['Зарплата'].min()
max_salary = df['Зарплата'].max()

print(f"Минимальная зарплата: {min_salary}")
print(f"Максимальная зарплата: {max_salary}")