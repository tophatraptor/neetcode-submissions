class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        most_freq = None
        freq_count = 0
        for x in nums:
            if freq_count == 0:
                most_freq = x
                freq_count = 1
            elif most_freq == x:
                freq_count += 1
            else:
                freq_count -= 1
        return most_freq