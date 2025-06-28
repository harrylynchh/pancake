'''
utils.py
2/28/2025
Harry Lynch
File containing all of the implementation-specific functions to solve the
Pancake problem
'''
import time
from cakes import PancakeStack
from priority import PriorityQueue
from globals import get_compare

'''
runAndPrint
Call the search function and print formatted results with time, sequence of flips,
Number of states assessed, and the final configuration.
'''
def runAndPrint(initialCake: PancakeStack, usingAStar: bool ) -> None:
    # Time the search and collect the size of the visited set and 
    # the final PancakeStack returned
    start = time.time()
    final, ctr = runSearch(initialCake)
    end = time.time()
    # Print results
    print("--------------------------------------------------------------------")
    print(f"Final Results for {'A*' if usingAStar else 'UCS'}:\nFlips: {final.flips}\nArray: {final.stack}")
    print(f"Time: {end - start}\nStates Accessed: {ctr}")
    print("--------------------------------------------------------------------")
'''
calculateHeuristic
Utility to calculate the gap heuristic, defined as number of stack positions for
which the pancake at that position is not of adjacent size to the pancake below
'''
def calculateHeuristic(stk: list) -> int:
    ctr = 0
    for i in range(1, len(stk) - 1):
        if (abs(stk[i] - stk[i+1]) > 1):
            ctr += 1
    return ctr;

'''
flip
Executes a flip of n_cakes pancakes within the stack, which effectively reverses
indices 0-n in the array. This is the core action that the agent takes
'''
def flip(curr: PancakeStack, n_cakes: int) -> PancakeStack:
        newStack = PancakeStack(curr.stack)
        if n_cakes >= len(newStack) or n_cakes <= 0:
            print("Error: Requested flip is out of bounds or flips the plate")
            return None
        start = 0
        end = n_cakes - 1
        newStack.cost = curr.cost + 1
        # Update the steps taken for this state
        newStack.flips = curr.flips + [n_cakes]
        # Swap the indices using 'tuple unpacking' with a two pointer approach
        # NOTE: learned about this on stack overflow. 
        while start < end:
            newStack.stack[start], newStack.stack[end] = newStack.stack[end], newStack.stack[start]
            start += 1
            end -= 1
        newStack.heuristic = calculateHeuristic(newStack.stack)
        return newStack

'''
promptUser
Handles user input for a given prompt and multiple-choice options 
'''
def promptUser(prompt: str, options: tuple) -> str:
    choice = None
    while choice not in options:
        choice = input(f"{prompt} {options} ")
        if choice not in options:
          print(f"Unexpected input, please specify one of these options: {options}")
    return choice

'''
collectInitialStack
Directs the user on how to provide input for the starting configuration and 
collects/parses said input
'''
def collectInitialStack() -> list:
    print("\nPlease input a SPACE-SEPARATED sequence of numbers to represent the stack PLATE included.")
    print("Note that this input is not sanitized so poor inputs will result in errors or improper results\n")
    confirmed = False
    
    while not confirmed:
        res = input("Please list the SPACE-SEPARATED values here or N for none (A randomly generated stack will be created of size 10): ")
        if res == 'N':
            return None
        confirmed = input(f"Is this your desired list (Y/N)?\n{res.split(' ')}") == 'Y'  
    # Cast all strings to ints in the split array and return that
    return [int(x) for x in res.split(' ')] 

'''
runSearch
Polymorphic search algorithm that supports both UCS and A* depending entirely
on the compare function set in globals.py (COMPARE_FN). Returns a tuple 
containing the stack object and the number of nodes visited
'''
def runSearch(initialCake: PancakeStack) -> tuple[PancakeStack, int]:
    # Define the goal as the sorted version of the initial stack, see note below
    goal = sorted(initialCake.stack)
    # Get COMPARE_FN from globals
    pq = PriorityQueue(get_compare())
    visited = set()
    pq.push(initialCake)
    while not pq.isEmpty():
        curr_best = pq.pop()
        # Check if curr best is goal NOTE: would check for heuristic == 0 but
        # for this to work for both UCS and A* simply need to check the configuration
        if curr_best.stack == goal:
            return (curr_best, len(visited))
        # Check if we've already seen curr_best, if so don't expand it's children
        if tuple(curr_best.stack) in visited:
            continue
        visited.add(tuple(curr_best.stack))
        # Foreach possible child configuration, add to the pq
        for i in range(2, len(curr_best)):
            pq.push(flip(curr_best, i))
    return None