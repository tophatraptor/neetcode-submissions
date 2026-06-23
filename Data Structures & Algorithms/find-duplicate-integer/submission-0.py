class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            if x not in seen:
                seen.add(x)
            else:
                return x