#!python3

import itertools
import string
import random


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

names = [name.title() for name in NAMES]
print(names)


names2 = [' '.join(name.split()[::-1]).title() for name in NAMES]
print(names2)

single_names2 = [name.split()[0].title() for name in NAMES]
print(f'Single Names List is: {single_names2}')

item1, item2 = ["one", "two"]
print(f'{item1}, {item2}')


def gen_pairs():
    single_names = [name.split()[0].title() for name in NAMES]
    while len(single_names) > 1:

        first, second = None, None
        while first == second:
            first, second = [single_names.pop(random.randrange(0, len(single_names) - 1)),
                             single_names.pop(random.randrange(0, len(single_names) - 1))]
        yield f"{first} teams up with {second}"


pairs = gen_pairs()
for _ in range(10):
    try:
        print(next(pairs))
    except StopIteration:
        print("Sorry no more pairs")
        break

