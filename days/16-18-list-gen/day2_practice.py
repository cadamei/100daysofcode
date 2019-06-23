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


def gen_pairs():
    single_names = [name.split()[0].title() for name in NAMES]
    dual_names = [single_names.pop(random.randrange(0, len(single_names) - 1)),
                  single_names.pop(random.randrange(0, len(single_names) - 1))]

    for pair in single_names:
        yield f"{single_names.pop(random.randrange(0, len(single_names) - 1))} teams up with " \
            f"{single_names.pop(random.randrange(0, len(single_names) - 1))}"


pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))
