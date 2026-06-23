class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        write_cursor = 1
        while write_cursor < len(nums) and nums[write_cursor - 1] != nums[write_cursor]:
            write_cursor += 1
        if write_cursor == len(nums):
            return len(nums) # all elements already unique
        read_cursor = write_cursor
        while read_cursor < len(nums) and nums[read_cursor] == nums[write_cursor]:
            read_cursor += 1
        if read_cursor == len(nums):
            return write_cursor
        
        while read_cursor < len(nums):
            # Top of the loop, assume that read_cursor and write_cursor are pointed at valid indices
            nums[write_cursor] = nums[read_cursor]
            while read_cursor < len(nums) and nums[read_cursor] == nums[write_cursor]:
                read_cursor += 1
            write_cursor += 1
        return write_cursor
