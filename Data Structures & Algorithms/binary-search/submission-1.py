class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        lower = 0
        upper = len(nums) - 1
        while lower <= upper:
            pivot = (upper - lower) // 2 + lower
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                upper = pivot - 1
            else:
                lower = pivot + 1
        # if nums[lower] == target:
        #     return upper
        return -1