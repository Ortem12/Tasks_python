# Начальный баланс счета
balance = 0

# История действий
history = []

# Основной цикл программы
while True:
    # Вывод меню
    print("\nВыберите действие:")
    print("1. Пополнить счет")
    print("2. Снять деньги")
    print("3. Проверить баланс")
    print("4. Выйти")

    # Ввод команды от пользователя
    choice = input("Ваш выбор (1/2/3/4): ")

    # Обработка выбора
    if choice == "1":
        # Пополнение счета
        amount = float(input("Введите сумму для пополнения: "))
        if amount > 0:
            balance += amount
            history.append(f"Счет пополнен на {amount}. Текущий баланс: {balance}")
            print(history[-1])  # Вывод последнего действия
        else:
            print("Сумма должна быть положительной.")

    elif choice == "2":
        # Снятие денег
        amount = float(input("Введите сумму для снятия: "))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                history.append(f"Со счета снято {amount}. Текущий баланс: {balance}")
                print(history[-1])  # Вывод последнего действия
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Сумма должна быть положительной.")

    elif choice == "3":
        # Проверка баланса
        history.append(f"Текущий баланс: {balance}")
        print(history[-1])  # Вывод последнего действия

    elif choice == "4":
        # Выход из программы
        print("Выход из программы. Спасибо за использование нашего сервиса!")
        break

    else:
        # Неверный выбор
        print("Неверный выбор. Пожалуйста, выберите действие из списка.")