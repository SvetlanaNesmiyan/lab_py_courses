def find_unique_value(some_list):
    for number in some_list:
        if some_list.count(number) == 1:
            return number

result = find_unique_value([5, 5, 5, 2, 2, 0.5])
print(result)