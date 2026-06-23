class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        alphanumeric = set("abcdefghijklmnopqrstuvwxyz0123456789")
        while i < j:
            if s[i] not in alphanumeric:
                i += 1
                continue
            if s[j] not in alphanumeric:
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True