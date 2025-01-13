import string

input_data = input("Введіть дві літери через дефіс:")

start, end = input_data.split('-')

letters = string.ascii_letters

start_index = letters.index(start)
end_index = letters.index(end)

print("".join(letters[start_index:end_index + 1]))