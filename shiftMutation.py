<<<<<<< HEAD
# Shift mutation is moving a gene from a randomly selected position
# by a random number of positions to the left or right.
=======
# Shift Mutation - Bounded Shifting Approach

"""
Shift mutation is  moving a gene from a randomly selected position by
a random number of positions to the left or right.
There are several approaches of implementing
shift mutation: bounded and unbounded
"""
>>>>>>> ec3fb81 (Update README.md)

import copy
import random
from math import copysign


<<<<<<< HEAD
def mutation_shift(ind):
=======
def shiftMutation(ind):
>>>>>>> ec3fb81 (Update README.md)
    mutation = copy.deepcopy(ind)
    position = random.sample(range(0, len(mutation)), 2)
    g1 = mutation[position[0]]
    dir = int(copysign(1, position[1] - position[0]))
    for i in range(position[0], position[1], dir):
        mutation[i] = mutation[i + dir]
    mutation[position[1]] = g1
    return mutation

<<<<<<< HEAD
random.seed(40)

ind = list(range(1,6))
mutation = mutation_shift(ind)
=======

random.seed(20)
ind = list(range(1,6))
mutation = shiftMutation(ind) 
>>>>>>> ec3fb81 (Update README.md)
print(f'Original: {ind}')
print(f'Mutated: {mutation}')