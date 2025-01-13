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

    day_word = "день" if days == 1 else ("дні" if 2 <= days <= 4 else "днів")
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