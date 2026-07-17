class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vtoi = {}
        for i, x in enumerate(nums):
            if target - x in vtoi:
                return [vtoi[target - x][0], i]
            else:
                if x in vtoi:
                    vtoi[x].append(i)
                else:
                    vtoi[x] = [i]