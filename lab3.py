def get_number():
    while number := input("Введите целое положительное число: "):
        try:
            _number = int(number)
        except ValueError:
            print("Введено не целое число")
        else:
            if _number < 0:
                print("Введено отрицательное число")
            else:
                return _number


def main():
    a, b = get_number(), get_number()
    print(f"Введены катеты прямоугольного треугольника {a} и {b}")
    print(f"Площадь равна {a * b / 2:.2f} и периметр равен {a * b * 2:.2f}")


if __name__ == "__main__":
    main()
