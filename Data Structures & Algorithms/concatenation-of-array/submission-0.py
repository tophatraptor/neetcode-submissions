class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = [None for _ in range(len(nums) * 2)]
        for i in range(len(nums) * 2):
            new_nums[i] = nums[i % len(nums)]
        return new_nums