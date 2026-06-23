class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        lower = 0
        upper = len(nums) - 1
        if nums[lower] < nums[upper]:
            # Array is sorted, minimum_element = None
            minimum_index = 0
        else:
            while lower <= upper:
                if lower == upper:
                    minimum_index = lower
                    break
                pivot = (upper - lower) // 2 + lower
                if pivot > 0 and nums[pivot - 1] > nums[pivot]:
                    minimum_index = pivot
                    break
                if nums[pivot] > nums[upper]:
                    # min element is in the right half
                    lower = pivot + 1
                else:
                    # min element is in the left half
                    upper = pivot - 1
            else:
                minimum_index = lower
        rotation = minimum_index
        non_rotated_lower = 0
        non_rotated_upper = len(nums) - 1
        while non_rotated_lower < non_rotated_upper:
            pivot = (non_rotated_upper - non_rotated_lower) // 2 + non_rotated_lower
            rpivot = (pivot + rotation) % len(nums)

            if nums[rpivot] == target:
                return rpivot
            elif nums[rpivot] > target:
                non_rotated_upper = pivot - 1
            else:
                non_rotated_lower = pivot + 1
        if nums[(non_rotated_lower + rotation) % len(nums)] != target:
            return -1
        return (non_rotated_lower + rotation) % len(nums)
        



"""
We can't just do if pivot < value because of the rotated matrix.

More straightforward solution: we first operate to find the index of the minimum element

Then we do a binary search using the rotated indices, also logn time

We want to find the index where for ordering a, b, c, a < b
"""