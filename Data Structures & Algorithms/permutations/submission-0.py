class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.permuteRecurse(nums, [], set(), res)
        return res

    def permuteRecurse(self, nums: List[int], candidate: List[int], selected_values: Set[int], res):
        if len(candidate) == len(nums):
            res.append(candidate[:])
        
        for i, x in enumerate(nums):
            if x not in selected_values:
                candidate.append(x)
                selected_values.add(x)
                self.permuteRecurse(nums, candidate, selected_values, res)
                candidate.pop()
                selected_values.remove(x)
