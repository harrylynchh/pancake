import random
class PancakeStack:
    stack: list
    heuristic: int
    cost: int
    def __init__(self, stk: list):
        self.stack = list(stk)
        self.heuristic = 0;
        self.cost = 0;