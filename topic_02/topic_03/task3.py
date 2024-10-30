def main():
    my_dict = {}
    
    while True:
        print("\nВиберіть функцію словника:")
        print("1. update()")
        print("2. del")
        print("3. clear()")
        print("4. keys()")
        print("5. values()")
        print("6. items()")
        print("7. Вихід")
        
        choice = input("Введіть номер функції: ")
        
        if choice == '1':
            key = input("Введіть ключ: ")
            value = input("Введіть значення: ")
            my_dict[key] = value  # Додаємо або оновлюємо ключ-значення
            print("Словник після update():", my_dict)
        
        elif choice == '2':
            key = input("Введіть ключ для видалення: ")
            try:
                del my_dict[key]
                print(f"Ключ '{key}' видалено.")
            except KeyError:
                print(f"Ключ '{key}' не знайдено.")
        
        elif choice == '3':
            my_dict.clear()
            print("Словник очищено.")
        
        elif choice == '4':
            print("Ключі в словнику:", list(my_dict.keys()))
        
        elif choice == '5':
            print("Значення в словнику:", list(my_dict.values()))
        
        elif choice == '6':
            print("Ключі та значення в словнику:", list(my_dict.items()))
        
        elif choice == '7':
            print("Вихід з програми.")
            break
        
        else:
            print("Невірний вибір!")

# Запуск програми
main()

