import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        heapq.heapify(nums)
        cur = heapq.heappop(nums)
        cur_length = 1
        longest_subsequence = 1
        while len(nums) > 0:
            next_val = heapq.heappop(nums)
            if next_val == cur + 1:
                cur_length += 1
                if cur_length > longest_subsequence:
                    longest_subsequence = cur_length
            elif next_val > cur + 1:
                cur_length = 1
            cur = next_val
        return longest_subsequence

"""
My first thought: we can use a hashmap, that represents the longest sequence ending at that element

However, I see from the second example: that elements can be added out of order. New plan - we can represent the seen state as a series of
intervals, each of which represents the start and end. We put both elements in the same dictionary.

When we encounter a new element, one of a few things happens:
- We create a new interval, of length 0 (e.x. [1, 1] for value 1)
- We expand an existing interval by one. When we do, we pop the key corresponding to the side of the interval we're expanding.

After expanding an existing interval by one: We check both sides of the interval to see if we can merge two intervals into one.

If we can, then we will pop three elements:
    - Either our min or max (depending on if we expanded to the left or right)
    - Both elements of the other array
    - We will then expand our interval object all the way to the popped min or max, and add another key

Lastly: We will check to see what the length of this interval is, and keep it as a list of intervals.

This solution is O(n)

Some more naive solutions to take a step back:
- We sort the array, then it becomes trivial to identify which sequences are long in O(n)
- We heapify, which is O(n), then start popping.
"""