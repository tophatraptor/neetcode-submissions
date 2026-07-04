class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        val_to_idx = {}
        for i, x in enumerate(nums):
            if x not in val_to_idx:
                val_to_idx[x] = []
            val_to_idx[x].append(i)
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = - nums[i] - nums[j]
                if target in val_to_idx:
                    for k in val_to_idx[target]:
                        if k != i and k != j:
                            res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                            break
        return [[i, j, k] for i, j, k in res]