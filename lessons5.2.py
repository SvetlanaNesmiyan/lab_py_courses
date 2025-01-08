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
            return num1 / num2
    else:
        return "Невказана операція"


while True:
    try:
        a = float(input("Введіть число: "))
        op = input("Виберіть дію(+, -, *, /): ")
        b = float(input("Введіть число: "))

        result = calculate(a, op, b)
        print("Результат:", result)

        continue_calculation = input("Продовжити?(так/y, ні/any key):")
        if continue_calculation.lower() not in ['так', 'y']:
            break
    except ValueError:
        print("Помилка: Неправильний ввід")