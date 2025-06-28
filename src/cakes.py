'''
cakes.py
2/28/2025
Harry Lynch
File containing the class definitions for the PancakeStack class, acting as a
node in this implementation
'''
from globals import get_compare
class PancakeStack:
    stack: list
    heuristic: int
    cost: int
    flips: list
    ''' Constructor '''
    def __init__(self, stk: list) -> None:
        import utils as utils
        self.stack = list(stk)
        self.heuristic = utils.calculateHeuristic(self.stack)
        self.flips = []
        self.cost = 0
        # Had to use heapq and I needed to define less than (__lt__) and needed
        # the same algorithm-dependent comparison fn so hence this member
        self.cmp = get_compare()
    ''' Length function'''
    def __len__(self) -> int:
        return len(self.stack)
    
    # Needed this for heapq- I had a previous implementation with a basic pq but
    # it was making my implementation slow over larger inputs
    ''' Less than operator overload for heapq '''
    def __lt__(self, other) -> bool:
        if type(self) != type(other):
            print(f"ERROR: TRYING TO COMPARE PancakeStack to {type(other)}")
            return False
        return self.cmp(self) < self.cmp(other)