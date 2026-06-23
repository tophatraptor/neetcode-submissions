class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        last_seen_word1 = -1
        last_seen_word2 = -1
        min_distance = len(wordsDict) + 1
        # Move forward through the list
        # Each time we see word1 or word2, we update index and recalculate
        # min distance
        for i, word in enumerate(wordsDict):
            if word == word1:
                last_seen_word1 = i
            if word == word2:
                last_seen_word2 = i
            if last_seen_word1 >= 0 and last_seen_word2 >= 0:
                diff = abs(last_seen_word2 - last_seen_word1)
                min_distance = min(diff, min_distance)
        return min_distance