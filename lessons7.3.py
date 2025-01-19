def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return None
    second_index = text.find(some_str, first_index + 1)
    return second_index if second_index != -1 else None

result = second_index("sims", "s")
print(result)