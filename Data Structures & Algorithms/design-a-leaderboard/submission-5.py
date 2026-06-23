import heapq
class Leaderboard:

    def __init__(self):
        self.scoremap = {}
        # playerId -> score, version
        self.heap = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scoremap:
            self.scoremap[playerId] = [score, 0]
            heapq.heappush(self.heap, (-score, playerId, 0))
            return
        self.scoremap[playerId][0] += score
        self.scoremap[playerId][1] += 1
        heapq.heappush(self.heap, (-self.scoremap[playerId][0], playerId, self.scoremap[playerId][1]))

    def top(self, K: int) -> int:
        num_scores = 0
        total = 0
        vals_to_repush = []
        while num_scores < K and len(self.heap) > 0:
            vals_to_repush.append(heapq.heappop(self.heap))
            neg_score, playerId, version = vals_to_repush[-1]
            if playerId not in self.scoremap:
                continue
            dict_version = self.scoremap[playerId][1]
            if dict_version != version:
                continue
            total -= neg_score
            num_scores += 1
        for x in vals_to_repush:
            heapq.heappush(self.heap, x)
        return total

    def reset(self, playerId: int) -> None:
        if playerId in self.scoremap:
            self.scoremap[playerId][0] = 0
            self.scoremap[playerId][1] += 1
            heapq.heappush(self.heap, (0, playerId, self.scoremap[playerId][1]))


# class Leaderboard:

#     def __init__(self):
#         self.scoremap = {}

#     def addScore(self, playerId: int, score: int) -> None:
#         if playerId not in self.scoremap:
#             self.scoremap[playerId] = score
#             return
#         self.scoremap[playerId] += score

#     def top(self, K: int) -> int:
#         scores = self.scoremap.values()
#         scores = list(sorted(scores, reverse=True))
#         return sum(scores[:K])

#     def reset(self, playerId: int) -> None:
#         if playerId in self.scoremap:
#             self.scoremap[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
