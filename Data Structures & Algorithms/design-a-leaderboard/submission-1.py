"""
Input:
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]

Output:
[null,null,null,null,null,null,73,null,null,null,141]
"""

"""
Failing test case:

["Leaderboard","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","addScore","top","reset","reset","addScore","reset"]
[[],[1,13],[2,93],[3,84],[4,6],[5,89],[6,31],[7,7],[8,1],[9,98],[10,42],[5],[1],[2],[3,76],[4,68],[1],[3],[4],[2,70],[2]]

My output:
[null,null,null,null,null,null,null,null,null,null,null,406,null,null,null,null,98,null,null,null,null]

Expected output:
[null,null,null,null,null,null,null,null,null,null,null,406,null,null,null,null,160,null,null,null,null]
"""

import heapq

class Leaderboard:

    def __init__(self):
        self.leaderBoard = {}
        self.heap = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderBoard:
            self.leaderBoard[playerId] = score
        else:
            self.leaderBoard[playerId] += score
        heapq.heappush(self.heap, (-self.leaderBoard[playerId], playerId))

    def top(self, K: int) -> int:
        viewed_results = []
        total = 0
        for i in range(K):
            neg_score, playerId = heapq.heappop(self.heap)
            while playerId not in self.leaderBoard or self.leaderBoard[playerId] != -neg_score: # if there is a mismatch between the heap and dictionary vlue, then pop
                neg_score, playerId = heapq.heappop(self.heap)
            viewed_results.append((-neg_score, playerId))
            total += -neg_score
        for score, playerId in viewed_results:
            heapq.heappush(self.heap, (-score, playerId))
        return total


    def reset(self, playerId: int) -> None:
        self.leaderBoard[playerId] = 0 # remove user from dict altogether


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

# V1 solution
# class Leaderboard:

#     def __init__(self):
#         self.leaderBoard = {}

#     def addScore(self, playerId: int, score: int) -> None:
#         self.leaderBoard[playerId] = score

#     def top(self, K: int) -> int:
#         heap = []
#         for player in self.leaderBoard:
#             heapq.heappush(heap, -self.leaderBoard[player])
        
#         total = 0
#         for i in range(K):
#             total += -heapq.heappop(heap)
#         return total


#     def reset(self, playerId: int) -> None:
#         self.leaderBoard.pop(playerId) # remove user from dict altogether

# V2 - before walk through and debug
# class Leaderboard:

#     def __init__(self):
#         self.leaderBoard = {}
#         self.heap = []

#     def addScore(self, playerId: int, score: int) -> None:
#         if playerId in self.leaderBoard and self.leaderBoard[playerId] == score:
#             continue
#         self.leaderBoard[playerId] = score
#         heapq.heappush(self.heap, (-score, playerId))

#     def top(self, K: int) -> int:
#         viewed_results = []
#         total = 0
#         for i in range(K):
#             neg_score, playerId = heaq.heappop(self.heap)
#             while self.leaderBoard[playerId] != -neg_score:
#                 neg_score, playerId = heapq.heappop(self.heap)
#             viewed_results.append((-neg_score, playerId))
#             total += -neg_score
#         for score, playerId in viewed_results:
#             self.heap.heappush((-score, playerId))
#         return total


#     def reset(self, playerId: int) -> None:
#         self.leaderBoard.pop(playerId) # remove user from dict altogether
