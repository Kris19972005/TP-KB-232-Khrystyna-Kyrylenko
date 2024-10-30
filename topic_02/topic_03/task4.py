def find_insert_position(sorted_list, element):
    """Пошук позиції для вставки елемента в відсортований список."""
    # Перевірка на пустий список
    if not sorted_list:
        return 0  # Якщо список порожній, вставка на позицію 0
    
    # Проходимо по списку
    for index in range(len(sorted_list)):
        # Якщо знайдено перший елемент, що більший або рівний новому
        if sorted_list[index] >= element:
            return index  # Повертаємо позицію для вставки
    
    # Якщо всі елементи менші, вставка в кінець списку
    return len(sorted_list)

# Приклад використання
sorted_list = [1, 3, 5, 7, 9]
new_element = 6

position = find_insert_position(sorted_list, new_element)
print(f"Позиція для вставки {new_element}: {position}")

# Додати елемент до списку за отриманою позицією
sorted_list.insert(position, new_element)
print("Оновлений список:", sorted_list)
