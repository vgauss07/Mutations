# Exchange Mutation
"""
Mutation exchange is applied to a binary or ordered set of genes.
A pair of genes are exchanged from randomly selected positions.
"""
import copy
import random


def mutation_exchange(ind):
    mutation = copy.deepcopy(ind)
    position = random.sample(range(0, len(mutation)), 2)
    g1 = mutation[position[0]]
    g2 = mutation[position[1]]
    mutation[position[1]] = g1
    mutation[position[0]] = g2
    return mutation

# Instance
random.seed(1)

ind = list(range(1, 7))
mutation = mutation_exchange(ind)

print(f'Original: {ind}')
print(f'Mutated: {mutation}')