class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        cur_square = 1
        while cur_square ** 2 <= n:
            squares.append(cur_square ** 2)
            cur_square += 1
        num_integers = [n for i in range(n + 1)]
        # From 0 to n, what is the minimum number of squares needed to reach that number
        num_integers[0] = 0
        for c in range(len(num_integers)):
            for s in squares:
                if c + s > n:
                    continue
                if num_integers[c + s] > num_integers[c] + 1:
                    num_integers[c + s] = num_integers[c] + 1
        return num_integers[-1]

# end of first loop num_integers: [0, 1, 6, 6, 1, 6, 6]
# end of c = 2 loop num_integers: [0, 1, 2, 6, 1, 2, 6]
# end of c = 3 loop num_integers: [0, 1, 2, 3, 1, 2, 3]
# end of c = 4 loop num_integers: [0, 1, 2, 3, 1, 2, 3]

# Version 1:
# class Solution:
#     def numSquares(self, n: int) -> int:
#         squares = []
#         cur_square = 1
#         while cur_square ** 2 < n:
#             squares.append(cur_square ** 2)
#             cur_square += 1
#         num_integers = [n for i in range(n + 1)]
#         # From 0 to n, what is the minimum number of squares needed to reach that number
#         num_integers[0] = 0
#         for c in range(len(num_integers)):
#             for s in squares:
#                 if c + s > n:
#                     continue
#                 if num_integers[c + s] < num_integers[c] + 1:
#                     num_integers[c + s] = num_integers[c] + 1
#         return num_integers[-1]