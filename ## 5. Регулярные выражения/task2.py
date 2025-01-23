import re
from datetime import datetime

def extract_and_format_dates(text):
    # Регулярное выражение для поиска дат в формате "Month Day, Year" (например, February 14, 2022)
    date_pattern1 = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b'
    
    # Регулярное выражение для поиска дат в формате "DD.MM.YYYY" (например, 23.03.2022)
    date_pattern2 = r'\b\d{2}\.\d{2}\.\d{4}\b'
    
    # Ищем все даты в тексте
    dates1 = re.findall(date_pattern1, text)  # Даты в формате "Month Day, Year"
    dates2 = re.findall(date_pattern2, text)  # Даты в формате "DD.MM.YYYY"
    
    # Преобразуем даты из формата "Month Day, Year" в "DD.MM.YYYY"
    formatted_dates = []
    for date in dates1:
        # Преобразуем строку в объект datetime
        dt = datetime.strptime(date, '%B %d, %Y')
        # Форматируем в "DD.MM.YYYY"
        formatted_dates.append(dt.strftime('%d.%m.%Y'))
    
    # Добавляем даты в формате "DD.MM.YYYY" (они уже в нужном формате)
    formatted_dates.extend(dates2)
    
    return formatted_dates

# Пример текста
input_text = """
On February 14, 2022, a long-awaited meeting took place between two organizations that had been planning a joint project for years. The discussions continued well into the evening, and by 23.03.2022, a draft agreement was ready for review. Despite some setbacks over the summer, significant progress was made, culminating in a final decision on 10.11.2022 to proceed with the implementation phase.

The following year saw rapid development, with major milestones achieved by January 15, 2023, and 04.04.2023. However, an unexpected delay arose on July 19, 2023, prompting a reassessment of the project timeline. Adjustments were made, and by 30.09.2023, the team was back on track, ready for the next phase of the initiative.
"""

# Извлечение и форматирование дат
dates = extract_and_format_dates(input_text)

# Вывод результата
print("Найденные даты в формате DD.MM.YYYY:")
for date in dates:
    print(date)