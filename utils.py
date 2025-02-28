import time
from cakes import PancakeStack
from priority import PriorityQueue
from globals import get_compare
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
def calculateHeuristic(stk: list) -> int:
    ctr = 0
    for i in range(1, len(stk) - 1):
        if (abs(stk[i] - stk[i+1]) > 1):
            ctr += 1
    return ctr;

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
        while start < end:
            newStack.stack[start], newStack.stack[end] = newStack.stack[end], newStack.stack[start]
            start += 1
            end -= 1
        newStack.heuristic = calculateHeuristic(newStack.stack)
        return newStack

def promptUser(prompt: str, options: tuple) -> str:
    choice = None
    while choice not in options:
        choice = input(f"{prompt} {options} ")
        if choice not in options:
          print(f"Unexpected input, please specify one of these options: {options}")
    return choice

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

def runSearch(initialCake: PancakeStack) -> tuple[PancakeStack, int]:
    goal = sorted(initialCake.stack)
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
        for i in range(2, len(curr_best)):
            pq.push(flip(curr_best, i))
    return None