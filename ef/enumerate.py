# range function
import random as random

random_bits = 0

for i in range(64):
    if random.randint(0, 1):
        random_bits |= 1 << i
        print(random_bits)

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

for i, flavor in enumerate(flavor_list, 1):
    print('%d:%s' % (i, flavor))
