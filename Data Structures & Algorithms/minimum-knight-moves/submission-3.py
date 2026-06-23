from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        x = abs(x)
        y = abs(y)
        move_count = 1
        # Moves we haven't processed
        valid_moves = deque(self.validMoves(0, 0))
        visited = set()
        next_moves = deque()
        while True:
            # Break when we see our number
            # Move through valid moves
            while len(valid_moves) > 0:
                curx, cury = valid_moves.pop()
                if curx == x and cury == y:
                    return move_count
                new_moves = self.validMoves(curx, cury)
                for move in new_moves:
                    if move[0] < 0 or move[1] < 0:
                        continue
                    if (move[0], move[1]) in visited:
                        continue
                    if abs(move[0]) + abs(move[1]) > 305:
                        continue
                    next_moves.append(move)
                    visited.add(move)
            # At the end of the valid_moves while loop, we popped
            # Everything off of valid moves, and next_moves
            # Contains all the new spaces reachable
            valid_moves = next_moves
            next_moves = deque()
            move_count += 1

    def validMoves(self, x: int, y: int) -> int:
        return [
            (x - 1, y + 2),
            (x + 1, y + 2),
            (x + 2, y + 1),
            (x + 2, y - 1),
            (x + 1, y - 2),
            (x - 1, y - 2),
            (x - 2, y + 1),
            (x - 2, y - 1),
        ]

# Solution 1
# from collections import deque
# class Solution:
#     def minKnightMoves(self, x: int, y: int) -> int:
#         if x == 0 and y == 0:
#             return 0
#         move_count = 1
#         # Moves we haven't processed
#         valid_moves = deque(self.validMoves(0, 0))
#         visited = set()
#         next_moves = deque()
#         while True:
#             # Break when we see our number
#             # Move through valid moves
#             while len(valid_moves) > 0:
#                 curx, cury = valid_moves.pop()
#                 if curx == x and cury == y:
#                     return move_count
#                 if (curx, cury) in visited:
#                     continue
#                 visited.add((curx, cury))
#                 new_moves = self.validMoves(curx, cury)
#                 for move in new_moves:
#                     if (move[0], move[1]) in visited:
#                         continue
#                     if abs(move[0]) + abs(move[1]) > 305:
#                         continue
#                     next_moves.append(move)
#             # At the end of the valid_moves while loop, we popped
#             # Everything off of valid moves, and next_moves
#             # Contains all the new spaces reachable
#             valid_moves = next_moves
#             next_moves = deque()
#             move_count += 1

#     def validMoves(self, x: int, y: int) -> int:
#         return [
#             (x - 1, y + 2),
#             (x + 1, y + 2),
#             (x + 2, y + 1),
#             (x + 2, y - 1),
#             (x + 1, y - 2),
#             (x - 1, y - 2),
#             (x - 2, y + 1),
#             (x - 2, y - 1),
#         ]