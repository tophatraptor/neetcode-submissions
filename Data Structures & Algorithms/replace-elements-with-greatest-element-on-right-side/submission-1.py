class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_seen = arr[-1]
        arr[-1] = -1
        for i in reversed(range(len(arr) - 1)):
            cur_value = arr[i]
            arr[i] = max_seen
            max_seen = max(cur_value, max_seen)
        return arr