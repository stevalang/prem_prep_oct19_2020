from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)


'''
Write a function called series_of_flips, that has one parameter, n, which represents the number of coin flips. Return a list of the random coin flips.
if n=4, then something like this: ['H', 'H', 'T', 'H']
'''
def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips

# print(series_of_flips(4))


'''
Write a function called four_flip_sample_space that has no parameters. It should return a list of all possible outcomes for 4 coin flips.
[
    ['H', 'H', 'H', 'H'],
    ['H', 'H', 'H', 'T'],
    ['H', 'H', 'T', 'H']
    ...
    ['T', 'T', 'T', 'T']
]
'''
def four_flip_sample_space():
    pass