class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vtoi = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in vtoi:
                return [vtoi[diff][0], i]
            if x not in vtoi:
                vtoi[x] = []
            vtoi[x].append(i)