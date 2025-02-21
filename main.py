import random
from globals import *
from cakes import PancakeStack
pancakes = PancakeStack(10)
print(pancakes.stack)
pancakes.flip(6)
print(pancakes.stack)