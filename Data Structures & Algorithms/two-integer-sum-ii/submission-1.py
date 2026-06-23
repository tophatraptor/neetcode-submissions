class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            cursum = numbers[i] + numbers[j]
            if cursum == target:
                return [i + 1, j + 1]
            if cursum > target:
                j -= 1
            if cursum < target:
                i += 1
