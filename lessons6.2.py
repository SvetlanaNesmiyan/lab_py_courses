def format_time(seconds):
    if not (0 <= seconds < 8640000):
        return "Число має бути більше або дорівнює 0 і менше ніж 8640000."

    time_units = {
        "day": 86400,
        "hour": 3600,
        "minute": 60
    }

    days, remaining_seconds = divmod(seconds, time_units["day"])
    hours, remaining_seconds = divmod(remaining_seconds, time_units["hour"])
    minutes, remaining_seconds = divmod(remaining_seconds, time_units["minute"])

    def get_day_word(value):
        if value % 10 == 1 and value % 100 != 11:
            return "день"
        elif 2 <= value % 10 <= 4 and not (12 <= value % 100 <= 14):
            return "дні"
        else:
            return "днів"

    day_word = get_day_word(days)

    formatted_time = (
        f"{days} {day_word}, "
        f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(remaining_seconds).zfill(2)}"
    )

    return formatted_time

try:
    user_input = int(input("Введіть число:"))
    print(format_time(user_input))
except ValueError:
    print("Будь ласка, введіть ціле число.")