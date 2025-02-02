import numpy as np

# Пример данных о прибыли за каждый сезон (в условных единицах)
# Данные представлены в виде списка: [весна, лето, осень, зима]
profit_data = [12000, 15000, 11000, 9000]

# Преобразуем список в массив numpy
profit_array = np.array(profit_data)

# Находим индекс максимального значения (самого прибыльного сезона)
most_profitable_season_index = np.argmax(profit_array)

# Список сезонов
seasons = ['весна', 'лето', 'осень', 'зима']

# Определяем самый прибыльный сезон
most_profitable_season = seasons[most_profitable_season_index]

# Выводим результат
print(f"Самый прибыльный сезон: {most_profitable_season}")