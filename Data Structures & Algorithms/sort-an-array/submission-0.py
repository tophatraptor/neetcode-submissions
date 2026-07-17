class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        first_partition = self.sortArray(nums[:len(nums) // 2])
        second_partition = self.sortArray(nums[len(nums) // 2:])
        i = 0
        j = 0
        res = []
        while i < len(first_partition) or j < len(second_partition):
            if i == len(first_partition):
                res.append(second_partition[j])
                j += 1
                continue
            if j == len(second_partition):
                res.append(first_partition[i])
                i += 1
                continue
            
            if second_partition[j] < first_partition[i]:
                res.append(second_partition[j])
                j += 1
            else:
                res.append(first_partition[i])
                i += 1
        return res