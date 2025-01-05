import random

random_list = [random.randint(0, 100) for _ in range(random.randint(3, 10))]

if len(random_list) >= 3:
    new_list = [random_list[0], random_list[2], random_list[-2]]
else:
    new_list = random_list 

print(f"{random_list}) == {new_list}")