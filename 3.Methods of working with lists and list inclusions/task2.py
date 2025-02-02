def replace_first_last(lst):
    # Проверяем, пустой ли список
    if not lst:
        return []
    
    # Проверяем, содержит ли список только один элемент
    if len(lst) == 1:
        return ["SINGLE"]
    
    # Заменяем первый и последний элементы
    lst[0] = "START"
    lst[-1] = "END"
    
    return lst

# Ввод списка строк вручную
user_input = input("Введите элементы списка через запятую: ")

# Преобразуем ввод в список строк
input_list = [item.strip() for item in user_input.split(",")]

# Вызов функции
result = replace_first_last(input_list)

# Вывод результата
print("Результат обработки списка:")
print(result)