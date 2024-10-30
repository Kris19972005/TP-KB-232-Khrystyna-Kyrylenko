def main():
    my_list = []
    
    while True:
        print("\nВиберіть функцію списку:")
        print("1. extend()")
        print("2. append()")
        print("3. insert()")
        print("4. remove()")
        print("5. clear()")
        print("6. sort()")
        print("7. reverse()")
        print("8. copy()")
        print("9. Вихід")
        
        choice = input("Введіть номер функції: ")
        
        if choice == '1':
            elements = input("Введіть елементи (через кому): ").split(',')
            my_list.extend([el.strip() for el in elements])
        
        elif choice == '2':
            value = input("Введіть значення для додавання: ")
            my_list.append(value)
        
        elif choice == '3':
            index = int(input("Введіть індекс: "))
            value = input("Введіть значення: ")
            my_list.insert(index, value)
        
        elif choice == '4':
            value = input("Введіть значення для видалення: ")
            try:
                my_list.remove(value)
            except ValueError:
                print(f"Значення '{value}' не знайдено.")
        
        elif choice == '5':
            my_list.clear()
            print("Список очищено.")
        
        elif choice == '6':
            try:
                my_list.sort()
            except Exception as e:
                print(f"Помилка при сортуванні: {e}")
        
        elif choice == '7':
            my_list.reverse()
        
        elif choice == '8':
            copied_list = my_list.copy()
            print("Скопійований список:", copied_list)
        
        elif choice == '9':
            print("Вихід з програми.")
            break
        
        else:
            print("Невірний вибір!")

        print("Поточний список:", my_list)

# Запуск програми
main()

