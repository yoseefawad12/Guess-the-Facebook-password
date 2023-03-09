import random

random_numbers = []

for i in range(100000000000):
    random_numbers.append(random.randint(1, 1000000000))

print(random_numbers)
