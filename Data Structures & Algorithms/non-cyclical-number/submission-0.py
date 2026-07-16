class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            new_n = 0
            while n > 0:
                new_n += (n % 10) ** 2
                n = n // 10
            n = new_n
            if n in seen:
                return False
        if n == 1:
            return True
        return False