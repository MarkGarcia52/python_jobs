import random as randint
import plotly.express as px

class Die:
    """Make a die class."""

die = Die()

def __init__(self, six_sided=6):
    """We initialize the variables, assuming a six-sided die."""
    self.six_sided = six_sided

def roll(self):
    """Roll a random value between 1 and 6"""
    return randint(1, self.six_sided)

