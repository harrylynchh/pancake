import utils as utils
class PancakeStack:
    stack: list
    heuristic: int
    cost: int
    def __init__(self, stk: list):
        self.stack = list(stk)
        self.heuristic = utils.calculateHeuristic(self.stack);
        self.cost = 0;
    def __len__(self):
        return len(self.stack)