from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        tuples_count = sorted([(ct[x], x) for x in ct], reverse = True)
        return [x[1] for x in tuples_count[:k]]