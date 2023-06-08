# Shift mutation is moving a gene from a randomly selected position
# by a random number of positions to the left or right.
# Shift Mutation - Bounded Shifting Approach

"""
Shift mutation is  moving a gene from a randomly selected position by
a random number of positions to the left or right.
There are several approaches of implementing
shift mutation: bounded and unbounded
"""


import copy
import random
from math import copysign

def shiftMutation(ind):
    mutation = copy.deepcopy(ind)
    position = random.sample(range(0, len(mutation)), 2)
    g1 = mutation[position[0]]
    dir = int(copysign(1, position[1] - position[0]))
    for i in range(position[0], position[1], dir):
        mutation[i] = mutation[i + dir]
    mutation[position[1]] = g1
    return mutation


random.seed(20)
ind = list(range(1,6))
mutation = shiftMutation(ind)
print(f'Original: {ind}')
print(f'Mutated: {mutation}')