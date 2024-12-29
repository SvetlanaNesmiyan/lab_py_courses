def split_list(lst):
    mid = (len(lst) + 1) // 2 

    return [lst[:mid], lst[mid:]]

examples_list = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1],
    []
]

for example in examples_list:
    print(f"{example} => {split_list(example)}")