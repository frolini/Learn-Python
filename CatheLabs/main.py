input_str = input("Введите выражение: ")
parts = input_str.split()

if len(parts) != 5:
    print("Неверный формат ввода")
else:
    a = float(parts[0])
    z1 = parts[1]
    b = float(parts[2])
    z2 = parts[3]
    c = float(parts[4])

    def calc(a, z1, b):
        if z1 in ('+', '-', '*', '/'):
            if z1 == '+':
                return a + b
            elif z1 == '-':
                return a - b
            elif z1 == '*':
                return a * b
            elif z1 == '/':
                return a / b
        else:
            print("Неверная операция")

    r = calc(a, z1, b)

    result = calc(r, z2, c)

    print(result)
    print(format(result, '.1f'))
    print(f"{result}")