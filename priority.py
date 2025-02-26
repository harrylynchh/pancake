from typing import Callable
from cakes import PancakeStack
class PriorityQueue:
    compare: Callable[[PancakeStack], int]
    queue: list
    def __init__(self, cmp: Callable[[PancakeStack], int]):
        self.compare = cmp
        self.queue = []
    
    def set_compare_fn(self, cmp: Callable[[PancakeStack], int]):
        self.compare = cmp;
    
    def push(self, data: PancakeStack):
        self.queue.append(data)
    
    def pop(self) -> PancakeStack:
        self.queue.sort(key=self.compare)
        return self.queue.pop(0);
    