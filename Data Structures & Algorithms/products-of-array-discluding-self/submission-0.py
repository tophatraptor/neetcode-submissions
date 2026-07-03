class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = []
        c = 1
        for x in nums:
            left_prefix.append(c)
            c = c * x
        c = 1
        right_prefix = []
        for x in reversed(nums):
            right_prefix.append(c)
            c = c * x
        right_prefix = right_prefix[::-1]
        res = [0 for _ in range(len(nums))]
        res[0] = right_prefix[0]
        res[-1] = left_prefix[-1]
        for i in range(len(res)):
            res[i] = left_prefix[i] * right_prefix[i]
        return res