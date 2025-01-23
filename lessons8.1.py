def add_one(some_list):
    number = int("".join(map(str, some_list)))
    number += 1
    return [int(digit) for digit in str(number)]


result = add_one([1, 2, 3, 4])
print(result)