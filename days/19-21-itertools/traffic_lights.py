#!python3

import itertools
import sys
import time

lights = 'green amber red'.split()
light_cycle = itertools.cycle(lights)


while True:
    sys.stdout.write('\r' + next(light_cycle))
    sys.stdout.flush()
    time.sleep(1)




