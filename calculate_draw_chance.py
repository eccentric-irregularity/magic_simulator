#!/usr/bin/env python3

from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

"""
https://docs.magicthegathering.io/
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy.stats import hypergeom

# This returns what it says but the issue is it won't handle more complex
# conditions such as must draw this by turn 3, this by turn 4 and have
# these lands available, this is going to be more tricky, I either need to
# get more involved in the stats or bruteforce the whole thing
def draw(number_in_deck, number_of_the_required_card_in_deck, cards_to_draw, number_that_atleast_must_be_drawn):
    M = number_in_deck
    n = number_of_the_required_card_in_deck
    N = cards_to_draw
    x = np.arange(0, n+1)
    pmf_card = hypergeom.pmf(x, M, n, N)

    chance_at_least_that_many_were_drawn = np.sum(pmf_card[number_that_atleast_must_be_drawn:])

    return chance_at_least_that_many_were_drawn


"""
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.hypergeom.html
[M, n, N] = [20, 7, 12]
rv = hypergeom(M, n, N)
x = np.arange(0, n+1)
pmf_dogs = rv.pmf(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, pmf_dogs, 'bo')
ax.vlines(x, 0, pmf_dogs, lw=2)
ax.set_xlabel('# of dogs in our group of chosen animals')
ax.set_ylabel('hypergeom PMF')
plt.show()
"""
