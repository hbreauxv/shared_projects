import random

random = {'rand': 'rand', 'rand2': 'rand2'}

for i in range(5):
    x = random.choice(list(random.items()))
    print(x)
