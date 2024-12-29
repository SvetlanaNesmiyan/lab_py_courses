def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Ділення на нуль неможливе."
        else:
            return a / b
    else:
        return "Невказана операція"


try:
    a = float(input("Введіть число: "))

    op = input("Виберіть дію(+, -, *, /): ")

    b = float(input("Введіть число: "))

    result = calculate(a, op, b)

    print("Результат:", result)

except ValueError:
    print("Помилка: Непраильний ввод")