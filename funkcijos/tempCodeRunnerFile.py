import random
test_list = [0, 1, 2]

for test in range(4):
    print(test_list[random.randint(0, len(test_list)-1)])
    