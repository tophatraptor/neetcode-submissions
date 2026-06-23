class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None for _ in range(capacity)]
        self.len = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.len == len(self.array):
            self.resize()
        self.array[self.len] = n
        self.len += 1

    def popback(self) -> int:
        val_to_ret = self.array[self.len - 1]
        self.len -= 1
        self.array[self.len] = None
        return val_to_ret

    def resize(self) -> None:
        new_array = [None for _ in range(2 * len(self.array))]
        for i, x in enumerate(self.array):
            new_array[i] = x
        self.array = new_array

    def getSize(self) -> int:
        return self.len
    
    def getCapacity(self) -> int:
        return len(self.array)