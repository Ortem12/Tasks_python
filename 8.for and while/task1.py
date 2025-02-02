import random
import string

def generate_password(length, use_letters=True, use_digits=False, use_special_chars=False):
    # Определяем набор символов для генерации пароля
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # Буквы (верхний и нижний регистр)
    if use_digits:
        characters += string.digits  # Цифры
    if use_special_chars:
        characters += string.punctuation  # Специальные символы

    # Генерация пароля
    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

# Ввод данных от пользователя
length = int(input("Введите длину пароля: "))
print("Выберите тип символов:")
print("1. Только буквы")
print("2. Буквы и цифры")
print("3. Буквы, цифры и специальные символы")
choice = int(input("Ваш выбор (1/2/3): "))

# Настройка параметров генерации в зависимости от выбора пользователя
if choice == 1:
    password = generate_password(length, use_letters=True, use_digits=False, use_special_chars=False)
elif choice == 2:
    password = generate_password(length, use_letters=True, use_digits=True, use_special_chars=False)
elif choice == 3:
    password = generate_password(length, use_letters=True, use_digits=True, use_special_chars=True)
else:
    print("Неверный выбор. Используются только буквы.")
    password = generate_password(length, use_letters=True, use_digits=False, use_special_chars=False)

# Вывод результата
print(f"Generated password: {password}")