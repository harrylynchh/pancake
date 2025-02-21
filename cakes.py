import random
class PancakeStack:
    stack: list
    def __init__(self, size: int):
        self.stack = list(range(1,size + 1))
        random.shuffle(self.stack)
    def flip(self, n: int) -> None:
        if n > len(self.stack) or n <= 0:
            print("ERR: OOB")
            return
        start = 0
        end = n - 1
        while start < end:
            print("S: " + str(start) + "    E: " + str(end))
            self.stack[start], self.stack[end] = self.stack[end], self.stack[start]
            start += 1
            end -= 1