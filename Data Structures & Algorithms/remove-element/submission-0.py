class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_cursor = 0
        while write_cursor < len(nums) and nums[write_cursor] != val:
            write_cursor += 1
        # Now, if it's in the list, we're pointing at the index
        read_cursor = write_cursor
        while read_cursor < len(nums) and nums[read_cursor] == val:
            read_cursor += 1
        # Now, read_cursor pointing at the first non-val element
        if read_cursor == len(nums):
            return write_cursor
        
        while read_cursor < len(nums):
            # Assume we have a valid starting index
            nums[write_cursor] = nums[read_cursor]
            write_cursor += 1
            read_cursor += 1
            # Fast forward to the first non-val element
            while read_cursor < len(nums) and nums[read_cursor] == val:
                read_cursor += 1
        return write_cursor