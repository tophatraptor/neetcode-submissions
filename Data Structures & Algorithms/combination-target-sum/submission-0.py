class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        return self.combinationSumTraverse(nums, target, [])

    def combinationSumTraverse(self, nums: List[int], target: int, prev: List[int]) -> List[List[int]]:
        if target < 0:
            return []
        if target == 0:
            return [prev]
        if prev is None:
            prev = nums[0]
        results = []
        for x in nums:
            if x <= target and (len(prev) == 0 or x >= prev[-1]):
                res = self.combinationSumTraverse(nums, target - x, prev + [x])
                results.extend(res)
        return results