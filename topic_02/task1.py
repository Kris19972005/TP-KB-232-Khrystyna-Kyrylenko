def calculate_discriminant(a, b, c):
    return b**2 - 4 * a * c

def find_roots(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return None  # Немає дійсних коренів

if __name__ == "__main__":
    a = float(input("Введіть коефіцієнт a: "))
    b = float(input("Введіть коефіцієнт b: "))
    c = float(input("Введіть коефіцієнт c: "))

    if a == 0:
        print("Коефіцієнт 'a' не може бути нулем.")
    else:
        roots = find_roots(a, b, c)
        if roots is None:
            print("Немає дійсних коренів.")
        elif len(roots) == 1:
            print("Є один корінь:", roots[0])
        else:
            print("Є два корені:", roots[0], "і", roots[1])
