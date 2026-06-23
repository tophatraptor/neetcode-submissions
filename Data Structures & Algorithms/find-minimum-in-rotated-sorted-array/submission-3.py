class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0
        upper = len(nums) - 1
        # The only case in which our first index is less than the
        # last element of the array, 
        if nums[lower] < nums[upper]:
            return nums[lower]
        while lower < upper:
            if upper - 1 == lower:
                return min(nums[lower], nums[upper])
            # We want to binary search for our index
            pivot = (upper - lower) // 2 + lower
            if nums[pivot - 1] > nums[pivot]:
                return nums[pivot]
            if nums[pivot] > nums[upper]:
                # Minimum after pivot
                lower = pivot + 1
            else:
                # minimum is before pivot
                upper  = pivot - 1
        return nums[lower]

"""
The pivot point is going to be the index of number b where
in the array, a > b < c

There are only two cases in which we can't cleanly check the above

The first, is that the pivot is the first element

We can check this directly by looking at our starting_index and making sure
that nums[0] < nums[-1]

In any rotated version, this is otherwise untrue.

Otherwise, there is some minimum where a > b, we actually don't need c
"""