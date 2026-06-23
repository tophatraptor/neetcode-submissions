class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        if len(nums) == 1:
            return False
        
        def canSum(start_index, target, nums: List[int]):
            if start_index == len(nums):
                return False
            if target < 0:
                return False
            if target == 0:
                return True
            return canSum(start_index + 1, target - nums[start_index], nums) or canSum(start_index + 1, target, nums)
        return canSum(0, total / 2, nums)
"""
The question is, does there exist a combination of results for
nums such that sum(pnums) == sum(nums) // 2?
"""