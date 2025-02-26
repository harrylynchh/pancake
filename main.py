import random
from globals import *
from cakes import PancakeStack
import utils as utils
from priority import PriorityQueue
finalFlipSequence = []
algoChoice = 'Z'
algoOptions = ('U', 'A')
utils.promptUser("Which sorting algorithm would you like to use?", algoChoice, algoOptions);
usingAStar = (algoChoice == 'A')
# Create an initial list 1..n and shuffle. Then add the plate at the end
initialStack = list(range(1, STACK_SIZE))
random.shuffle(initialStack)
initialStack.append(STACK_SIZE);
initialCakes = PancakeStack(initialStack);
# Set pq comparison fn depending on algorithm type
pq_fn = (lambda stack: stack.heuristic + stack.cost) if usingAStar \
        else (lambda stack: stack.heuristic)
queue = PriorityQueue(pq_fn);

print(initialCakes.stack)
print(utils.flip(initialCakes, 9).stack)