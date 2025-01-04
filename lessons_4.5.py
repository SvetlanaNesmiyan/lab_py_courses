array = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    []
]

for sublist in array:
    if sublist: 
        sum_even_indices = sum(sublist[i] for i in range(0, len(sublist), 2))
        result = sum_even_indices * sublist[-1]
    else:
        result = 0
    print(f"{sublist} -> {result}")
