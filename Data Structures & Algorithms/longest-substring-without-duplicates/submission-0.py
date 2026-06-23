class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wchar = set()
        start = 0
        end = 0
        maxlen = 0
        # Our indices are *not* inclusive, so [0, 1] means that we have just the character at index 0
        while end < len(s):
            if s[end] not in wchar:
                wchar.add(s[end])
                if len(wchar) > maxlen:
                    maxlen = len(wchar)
                end += 1
            else:
                while start < end and s[end] in wchar:
                    wchar.remove(s[start])
                    start += 1
        return maxlen