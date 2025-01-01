nums = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

for toolist in nums:
    list = toolist[:]
    non_zero_index = 0

    for i in range(len(toolist)):
        if toolist[i] != 0:
            toolist[non_zero_index] = toolist[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(toolist)):
        toolist[i] = 0
        
    print(f"{list} -> {toolist}")
