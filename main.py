import random
from globals import *
from cakes import PancakeStack
SIZE = 10
stack = list(range(1,SIZE + 1))
random.shuffle(stack)
def flip(stack: list, n: int) -> list:
        newStack = list(stack);
        if n > len(newStack) or n <= 0:
            print("ERR: OOB")
            return
        start = 0
        end = n - 1
        while start < end:
            newStack[start], newStack[end] = newStack[end], newStack[start]
            start += 1
            end -= 1
        return newStack
pancakes = PancakeStack(10)
print(pancakes.stack)
pancakes.flip(6)
print(pancakes.stack)