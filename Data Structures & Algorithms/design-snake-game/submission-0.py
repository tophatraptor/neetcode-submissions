class SnakeNode:
    def __init__(self, next_node, prev_node, r, c):
        self.next_node = next_node
        self.prev_node = prev_node
        self.r = r
        self.c = c

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.length = 1
        # Score = length - 1
        self.snake_head = SnakeNode(None, None, 0, 0)
        self.snake_tail = self.snake_head
        self.food_cursor = 0
        self.food = food
        self.width = width
        self.height = height
        self.snake_tiles = set()
        self.snake_tiles.add((0, 0))

    def move(self, direction: str) -> int:
        # First, derive next coordinate
        next_coord = [self.snake_head.r, self.snake_head.c]
        if direction == "R":
            next_coord[1] += 1
        elif direction == "U":
            next_coord[0] -= 1
        elif direction == "L":
            next_coord[1] -= 1
        elif direction == "D":
            next_coord[0] += 1
        
        next_coord = (next_coord[0], next_coord[1])
        # First: out of bounds
        if next_coord[0] < 0 or next_coord[0] >= self.height:
            return -1
        if next_coord[1] < 0 or next_coord[1] >= self.width:
            return -1
        
        # Next question: Is this a valid food? If so, just extend snake
        if self.food_cursor < len(self.food) and next_coord == (self.food[self.food_cursor][0], self.food[self.food_cursor][1]):
            new_head = SnakeNode(self.snake_head, None, next_coord[0], next_coord[1])
            self.snake_head.prev_node = new_head
            self.snake_head = new_head
            self.snake_tiles.add((next_coord[0], next_coord[1]))
            self.length += 1
            self.food_cursor += 1
            return self.length - 1
        
        # If it's not a food item, we will add a new node to the head
        # And remove one from the tail
        new_head = SnakeNode(self.snake_head, None, next_coord[0], next_coord[1])
        self.snake_head.prev_node = new_head
        self.snake_head = new_head
        self.snake_tiles.remove((self.snake_tail.r, self.snake_tail.c))
        self.snake_tail = self.snake_tail.prev_node
        if next_coord in self.snake_tiles:
            return -1
        self.snake_tiles.add(next_coord)
        return self.length - 1

# class SnakeNode:
#     def __init__(self, next_node, prev_node, r, c):
#         self.next_node = next_node
#         self.prev_node = prev_node
#         self.r = r
#         self.c = c

# class SnakeGame:

#     def __init__(self, width: int, height: int, food: List[List[int]]):
#         self.length = 1
#         # Score = length - 1
#         self.snake_head = SnakeNode(None, None, 0, 0)
#         self.snake_tail = self.snake_head
#         self.food_cursor = 0
#         self.food = food
#         self.width = width
#         self.height = height
#         self.snake_tiles = set()
#         self.snake_tiles.add((0, 0))

#     def move(self, direction: str) -> int:
#         # First, derive next coordinate
#         next_coord = [self.snake_head.r, self.snake_head.c]
#         if direction == "R":
#             next_coord[1] += 1
#         elif direction == "U":
#             next_coord[0] -= 1
#         elif direction == "L":
#             next_coord[1] -= 1
#         elif direction == "D":
#             next_coord[0] += 1
        
#         next_coord = (next_coord[0], next_coord[1])
#         # First: out of bounds
#         if next_coord[0] < 0 or next_coord[0] >= self.width:
#             return -1
#         if next_coord[1] < 0 or next_coord[1] >= self.height:
#             return -1
        
#         # Next question: Is this a valid food? If so, just extend snake
#         if self.food_cursor < len(self.food) and next_coord == self.food[food_cursor]:
#             new_head = SnakeNode(self.snake_head, None, next_coord[0], next_coord[1])
#             self.snake_head.prev_node = new_head
#             self.snake_head = new_head
#             self.snake_tiles.add((next_coord[0], next_coord[1]))
#             self.length += 1
#             self.food_cursor += 1
#             return self.length - 1
        
#         # If it's not a food item, we will add a new node to the head
#         # And remove one from the tail
#         new_head = SnakeNode(self.snake_head, None, next_coord[0], next_coord[1])
#         self.snake_head.prev_node = new_head
#         self.snake_head = new_head
#         self.snake_tiles.remove((self.snake_tail.r, self.snake_tail.c))
#         self.snake_tail = self.snake_tail.prev_node
#         if next_coord in self.snake_tiles:
#             return -1
#         self.snake_tiles.add(next_coord)
#         return self.length - 1
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

# O(1) to move
# O(1) to expand
# O(1) to check game states
# O(N * M) memory because of the snake length
