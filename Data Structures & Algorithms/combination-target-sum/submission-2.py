class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums = sorted(nums)
        def dfstraverse(i, nums: List[int], target: int, sequence: List[int]):
            if target < 0:
                return
            if target == 0:
                results.append(sequence[:])
                return
            for j in range(i, len(nums)):
                if nums[j] > target:
                    break
                sequence.append(nums[j])
                dfstraverse(j, nums, target - nums[j], sequence)
                sequence.pop()
        
        dfstraverse(0, nums, target, [])
        return results