from cakes import PancakeStack
from priority import PriorityQueue

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
        while start < end:
            newStack.stack[start], newStack.stack[end] = newStack.stack[end], newStack.stack[start]
            start += 1
            end -= 1
        newStack.heuristic = calculateHeuristic(newStack.stack)
        return newStack

def promptUser(prompt: str, choice: str, options: tuple) -> str:
    while choice not in options:
        choice = input(f"{prompt} {options} ")
        if choice not in options:
          print(f"Unexpected input, please specify one of these options: {options}")
    return choice

def runSearch(usingAStar: bool, initialCake: PancakeStack) -> tuple[list, PancakeStack]:
    pq_fn = (lambda stack: stack.heuristic + stack.cost) if usingAStar \
        else (lambda stack: stack.heuristic)
    queue = PriorityQueue(pq_fn);
    return runAStar(queue, initialCake, []) if usingAStar else runUCS(queue, initialCake, []);

def runAStar(queue: PriorityQueue, currStk: PancakeStack, flipList: list) -> tuple[list, PancakeStack]:
    
    return (flipList, currStk)

def runUCS(queue: PriorityQueue, currStk: PancakeStack, flipList: list) -> tuple[list, PancakeStack]:
    return (flipList, currStk)