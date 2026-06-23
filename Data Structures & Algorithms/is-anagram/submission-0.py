from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sct = Counter(s)
        tct = Counter(t)
        return sct == tct