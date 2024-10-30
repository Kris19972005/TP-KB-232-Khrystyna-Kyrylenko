def calculate_discriminant(a, b, c):
    return b**2 - 4 * a * c

if __name__ == "__main__":
    a = float(input("Введіть коефіцієнт a: "))
    b = float(input("Введіть коефіцієнт b: "))
    c = float(input("Введіть коефіцієнт c: "))

    if a == 0:
        print("Коефіцієнт 'a' не може бути нулем.")
    else:
        discriminant = calculate_discriminant(a, b, c)
        print("Дискримінант:", discriminant)



