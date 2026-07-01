from collections import deque
class Solution:
    def confusingNumber(self, n: int) -> bool:
        orig_number = n
        rotation_mapping = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6,
        }
        res = deque()
        while n > 0:
            digit = n % 10
            if digit not in rotation_mapping:
                return False
            res.append(digit)
            n = n // 10
        new_number = 0
        while len(res) > 0:
            digit = res.popleft()
            new_digit = rotation_mapping[digit]
            new_number = 10 * new_number + new_digit
        return new_number != orig_number