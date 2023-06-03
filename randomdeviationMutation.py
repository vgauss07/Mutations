# Random deviation mutation
"""
Random deviation mutation can be implemented by supplementing the random variable
with normal distribution (average = 0 and deviation = 1)
"""
import copy
import random


def mutation_random_deviation(ind, mu, sigma, p):
    mutation = copy.deepcopy(ind)
    # The deepcopy() function will create a deep copy of any object, including custom
    # objects and classes.
    for i in range(len(mutation)):
        if random.random() < p:
            mutation[i] = mutation[i] + random.gauss(mu, sigma)
        return mutation

# Instance
random.seed(0)
ind = [random.uniform(0, 10) for _ in range(2)]
mutation = mutation_random_deviation(ind, 0, 1, 0.3)
print(f'Original: {ind}')
print(f'Mutated: {mutation}')
