def move_last_to_first(lst):
    if len(lst) <= 1:
        return lst
    else:
        return [lst[-1]] + lst[:-1]

examples_list = [
    [12, 3, 4, 10],
    [1],
    [],
    [12, 3, 4, 10, 8]
]

for example in examples_list:
    print(f"{example} => {move_last_to_first(example)}")