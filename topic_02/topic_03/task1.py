def calculator():
    print("Калькулятор готовий до роботи!")
    print("Введіть 'exit' для виходу.")
    
    while True:
        try:
            # Запит на введення першого числа
            num1 = input("Введіть перше число: ")
            if num1.lower() == 'exit':
                print("Вихід з програми.")
                break
            
            num1 = float(num1)

            # Запит на введення операції
            operation = input("Введіть операцію (+, -, *, /): ")
            if operation.lower() == 'exit':
                print("Вихід з програми.")
                break

            # Запит на введення другого числа
            num2 = input("Введіть друге число: ")
            if num2.lower() == 'exit':
                print("Вихід з програми.")
                break
            
            num2 = float(num2)

            # Виконання обчислення
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Помилка: ділити на нуль не можна"
            else:
                result = "Невідома операція."

            print(f"Результат: {result}")

        except ValueError:
            print("Будь ласка, введіть коректне число.")

# Запуск калькулятора
calculator()
