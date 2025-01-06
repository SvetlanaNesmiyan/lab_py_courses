import random

random_list = [random.randint(0, 100) for _ in range(random.randint(3, 10))]

new_list = [random_list[0], random_list[2], random_list[-2]]

print(f"{random_list} > { new_list}")