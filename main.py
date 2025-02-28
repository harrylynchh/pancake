import random
from cakes import PancakeStack
import utils as utils
from globals import set_compare
# Prompt the user for an algorithm type
SIZE = 10
astar_fn = lambda stack: stack.heuristic + stack.cost
ucs_fn = lambda stack: stack.cost
algoOptions = ('U', 'A')
algoChoice = utils.promptUser("Which sorting algorithm would you like to use?", algoOptions)
usingAStar = (algoChoice == 'A')
set_compare(astar_fn if usingAStar else ucs_fn)
init = utils.collectInitialStack()
if init == None:
        init = list(range(1, SIZE))
        random.shuffle(init)
        init.append(SIZE)
# Create an initial configuration
initialCake = PancakeStack(init)
print(f"Initial Cake Orientation is: {initialCake.stack}")

utils.runAndPrint(initialCake, usingAStar)
rerunChoice = utils.promptUser("Would you like to rerun the same initial stack on the other sorting algorithm?", ('Y', 'N'))
if rerunChoice == 'Y':
        usingAStar = not usingAStar
        set_compare(astar_fn if usingAStar else ucs_fn) 
        utils.runAndPrint(initialCake, usingAStar)