class Leaderboard:

    def __init__(self):
        self.scoremap = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scoremap:
            self.scoremap[playerId] = score
            return
        self.scoremap[playerId] += score

    def top(self, K: int) -> int:
        scores = self.scoremap.values()
        scores = list(sorted(scores, reverse=True))
        return sum(scores[:K])

    def reset(self, playerId: int) -> None:
        if playerId in self.scoremap:
            self.scoremap[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
