nums = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

for alsoalist in nums:
    list = alsoalist[:]
    non_zero_index = 0

    for i in range(len(alsoalist)):
        if alsoalist[i] != 0:
            alsoalist[non_zero_index] = alsoalist[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(alsoalist)):
        alsoalist[i] = 0
        
    print(f"{list} -> {alsoalist}")
