def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "На нуль ділити не можна!"

def calculator():
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    
    choice = input("Введіть номер операції (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        match choice:
            case '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            case '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            case '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            case '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
    else:
        print("Невірний вибір! Будь ласка, виберіть номер від 1 до 4.")

if __name__ == "__main__":
    calculator()
