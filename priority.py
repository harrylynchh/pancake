'''
priority.py
2/28/2025
Harry Lynch
File containing definitions for the PriorityQueue class, the primary data structure
which depends on the standard library heapq for the heap logic.  The pq function
is a lambda dependent on what search type the user selects and is defined in
globals.py and originally in main.py
'''
import heapq
from typing import Callable
from cakes import PancakeStack
class PriorityQueue:
    compare: Callable[[PancakeStack], int]
    queue: list
    def __init__(self, cmp: Callable[[PancakeStack], int]):
        self.compare = cmp
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def isEmpty(self) -> bool:
        return len(self) == 0
    def set_compare_fn(self, cmp: Callable[[PancakeStack], int]):
        self.compare = cmp;
    
    def push(self, data: PancakeStack):
        priority = self.compare(data)
        heapq.heappush(self.queue, (priority, data))
    
    def pop(self) -> PancakeStack:
        if not self.isEmpty():
            # Grab the item from the heap priority queue, _ is a placeholder
            # since it returns a tuple.
            _, item = heapq.heappop(self.queue)
            return item;
        print("ERROR: ATTEMPTING TO POP FROM EMPTY STACK")
        return None
    