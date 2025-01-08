import string
import keyword

variable_name = input("Введіть рядок: ")

if variable_name[0].isdigit() or any(ch in string.punctuation.replace('_', '') or ch.isspace() for ch in variable_name):
    print(False)

elif any(ch.isupper() for ch in variable_name):
    print(False)

elif variable_name.count('_') > 1:
    print(False)

elif variable_name in keyword.kwlist:
    print(False)

else:
    print(True)