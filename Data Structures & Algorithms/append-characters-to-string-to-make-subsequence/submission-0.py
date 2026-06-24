class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_cursor = 0
        s_cursor = 0
        while s_cursor < len(s):
            if s[s_cursor] == t[t_cursor]:
                t_cursor += 1
                if t_cursor == len(t):
                    return 0
            s_cursor += 1
        
        # At this juncture, we should know how many letters in t are not contained in s
        return len(t) - t_cursor